"""编排：collect → analyze（写项目库）→ build_summary（写日报）。

不含推送（推送由 push.py 在 08:00 单独执行，错峰保证准时）。
"""
from __future__ import annotations

import argparse

from . import analyze, build_summary, collect, llm_client
from .config_loader import get_config
from .store import load_index, save_index
from .utils import get_logger, today_str

log = get_logger()


def run(top_n: int | None = None) -> dict:
    try:
        return _run(top_n)
    except Exception as e:
        log.exception("Pipeline 失败：%s", e)
        _alert_failure(e)
        raise


def _run(top_n: int | None = None) -> dict:
    if not llm_client.available():
        log.warning("当前无可用 LLM key：将跳过深度学习，仅采集+更新元数据。")

    candidates = collect.collect()

    top_n = top_n or get_config()["collect"]["top_n"]
    # 新项目：深度学习，受 top_n 限制（控制 LLM 成本）。
    new_items = [c for c in candidates if c["decision"] == "new"][:top_n]
    # 老项目（revisit / skip_lightweight）：全部交给 analyze 权威裁决。
    # analyze._should_revisit 会看 release/star 决定重学还是轻量更新，
    # 这样 on_new_release 才真正生效（修复 collect 粗判导致的逻辑割裂）。
    seen_items = [c for c in candidates if c["decision"] != "new"]
    log.info("本轮：新项目 %d（top_n=%d）+ 老项目复核 %d", len(new_items), top_n, len(seen_items))

    index = load_index()
    items = []
    processed = []  # 本轮成功 learn 的全部结果（含未进主日报的静默更新），供霸榜榜单用
    for c in new_items:
        try:
            res = analyze.learn(c, index)
            items.append(res)
            processed.append(res)
        except Exception as e:
            log.warning("处理 %s 失败：%s", c["full_name"], e)
    for c in seen_items:
        try:
            res = analyze.learn(c, index)
            processed.append(res)
            # 老项目仅在实际重学（出新 release / star 大涨）时才进日报，
            # 否则只静默更新 streak/metadata，避免日报被未变动项目刷屏。
            if res.get("refreshed"):
                items.append(res)
        except Exception as e:
            log.warning("复核 %s 失败：%s", c["full_name"], e)
    save_index(index)

    streaks = _streak_leaderboard(processed)
    news = _collect_news()
    payload = build_summary.build(items, streaks, news=news)
    log.info("Pipeline 完成。")
    return payload


def _collect_news() -> list[dict]:
    """AI 资讯并行轨：完全隔离，任何失败都不影响项目日报。"""
    try:
        from . import news_collect, news_summary
        candidates = news_collect.collect_news()
        if not candidates:
            return []
        news = news_summary.summarize(candidates)
        news_collect.mark_seen(news)
        return news
    except Exception as e:
        log.warning("资讯采集失败（不影响项目日报）：%s", e)
        return []


def _streak_leaderboard(processed: list[dict]) -> list[dict]:
    """从本轮处理结果里挑出「连续上榜 ≥ streak_min_days 天」的项目，
    按连续天数（再按总 star）降序，构成纯展示用的霸榜榜单。零额外 LLM 成本。"""
    min_days = get_config()["report"].get("streak_min_days", 3)
    hot = [r for r in processed if (r.get("streak_days") or 0) >= min_days]
    hot.sort(key=lambda r: (r.get("streak_days") or 0, r.get("stars_total") or 0),
             reverse=True)
    return hot


def _alert_failure(e: Exception) -> None:
    """pipeline 整体失败时推一条飞书告警，避免 08:00 静默无日报。"""
    try:
        from . import feishu_client
        feishu_client.send_alert(
            f"⚠️ AI 日报 · 采集失败 {today_str()}",
            ["凌晨流水线运行异常，08:00 可能无日报。",
             f"错误：`{type(e).__name__}: {e}`",
             "排查见 logs/。"],
        )
    except Exception as ee:
        log.warning("失败告警也发送失败：%s", ee)


def main():
    ap = argparse.ArgumentParser(description="AI 项目日报 pipeline（采集+学习+日报）")
    ap.add_argument("--top-n", type=int, default=None, help="本轮最多深度学习的项目数")
    args = ap.parse_args()
    run(top_n=args.top_n)


if __name__ == "__main__":
    main()
