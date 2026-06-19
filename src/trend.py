"""周热度趋势报告（二次报告）。

消费各项目 metadata.json 里的 appearances[] 时间序列，在统计窗口内聚合出
「本周最热 / 持续上榜 / 本周新晋」三张榜，写入 trends/<date>-weekly.(md|json)，
可选推送飞书。数据全部来自已落盘的 metadata，无需再调 GitHub/LLM。
"""
from __future__ import annotations

import argparse
import sys
from datetime import date, timedelta

from .config_loader import get_config
from .store import iter_project_metas, trends_root, write_json, write_text
from .utils import get_logger, now, today_str

log = get_logger()


def _to_date(s) -> date | None:
    try:
        y, m, d = (int(x) for x in str(s).split("-"))
        return date(y, m, d)
    except (ValueError, TypeError, AttributeError):
        return None


def _weekly_gain(apps_sorted: list[dict]) -> int:
    """窗口内 star 增量：优先用首尾 stars_total 之差；单点时退化为该次 stars_gained。"""
    first = apps_sorted[0].get("stars_total") or 0
    last = apps_sorted[-1].get("stars_total") or 0
    delta = last - first
    max_gained = max((a.get("stars_gained") or 0) for a in apps_sorted)
    return max(delta, max_gained, 0)


def aggregate(metas: list[dict], today: date, days: int = 7) -> dict:
    """把项目 metadata 聚合成趋势榜。纯函数，便于测试。"""
    window_start = today - timedelta(days=days)
    rows: list[dict] = []
    for m in metas:
        apps = [a for a in m.get("appearances", [])
                if (_to_date(a.get("date")) or date.min) > window_start]
        if not apps:
            continue
        apps_sorted = sorted(apps, key=lambda a: a.get("date", ""))
        first_seen = _to_date(m.get("first_seen"))
        rows.append({
            "full_name": m.get("full_name"),
            "url": m.get("url"),
            "one_liner": m.get("one_liner", ""),
            "why_worth_it": m.get("why_worth_it", ""),
            "tags": m.get("tags", []) or [],
            "language": m.get("language"),
            "stars_total": apps_sorted[-1].get("stars_total") or 0,
            "weekly_gain": _weekly_gain(apps_sorted),
            "appear_days": len({a.get("date") for a in apps}),
            "streak_days": m.get("streak_days", 1),
            "first_seen": m.get("first_seen"),
            "is_newcomer": bool(first_seen and first_seen > window_start),
            "latest_release": m.get("latest_release"),
        })

    hottest = sorted(rows, key=lambda r: (r["weekly_gain"], r["stars_total"]), reverse=True)
    rising = sorted([r for r in rows if r["appear_days"] >= 2],
                    key=lambda r: (r["appear_days"], r["weekly_gain"]), reverse=True)
    newcomers = sorted([r for r in rows if r["is_newcomer"]],
                       key=lambda r: (r["weekly_gain"], r["stars_total"]), reverse=True)
    return {"window_days": days, "total": len(rows),
            "hottest": hottest, "rising": rising, "newcomers": newcomers}


def _fmt_tags(tags: list) -> str:
    return ("　" + " ".join(f"`{t}`" for t in tags)) if tags else ""


def render_md(payload: dict, date_str: str, top_n: int) -> str:
    days = payload["window_days"]
    lines = [f"# 📈 AI 项目周趋势 · 截至 {date_str}", "",
             f"近 **{days}** 天内上榜 **{payload['total']}** 个项目。", ""]

    def section(title: str, rows: list[dict], metric):
        lines.append(f"## {title}")
        if not rows:
            lines.extend(["_本期无_", ""])
            return
        for i, r in enumerate(rows[:top_n], 1):
            lines.append(f"{i}. [{r['full_name']}]({r['url']}) — {metric(r)}"
                         f"{_fmt_tags(r['tags'])}")
            tip = r.get("why_worth_it") or r.get("one_liner")
            if tip:
                lines.append(f"   - {tip}")
        lines.append("")

    section("🔥 本周最热（star 增量）", payload["hottest"],
            lambda r: f"+{r['weekly_gain']}⭐（共 {r['stars_total']}）")
    section("📌 持续上榜（窗口内出现天数）", payload["rising"],
            lambda r: f"{r['appear_days']} 天 ｜ 连续 {r['streak_days']} 天 ｜ +{r['weekly_gain']}⭐")
    section("🆕 本周新晋", payload["newcomers"],
            lambda r: f"+{r['weekly_gain']}⭐（首见 {r['first_seen']}）")
    return "\n".join(lines)


def _build_card(payload: dict, date_str: str, top_n: int) -> dict:
    elements: list[dict] = []

    def block(title: str, rows: list[dict], metric):
        elements.append({"tag": "div", "text": {"tag": "lark_md", "content": f"**{title}**"}})
        if not rows:
            elements.append({"tag": "div", "text": {"tag": "lark_md", "content": "_本期无_"}})
        else:
            body = "\n".join(
                f"{i}. [{r['full_name']}]({r['url']}) {metric(r)}"
                for i, r in enumerate(rows[:top_n], 1))
            elements.append({"tag": "div", "text": {"tag": "lark_md", "content": body}})
        elements.append({"tag": "hr"})

    block("🔥 本周最热", payload["hottest"], lambda r: f"+{r['weekly_gain']}⭐")
    block("📌 持续上榜", payload["rising"], lambda r: f"{r['appear_days']}天/+{r['weekly_gain']}⭐")
    block("🆕 本周新晋", payload["newcomers"], lambda r: f"+{r['weekly_gain']}⭐")
    elements.append({"tag": "note", "elements": [
        {"tag": "lark_md", "content": f"📊 近 {payload['window_days']} 天上榜 {payload['total']} 个项目"}]})

    return {
        "config": {"wide_screen_mode": True},
        "header": {"template": "purple",
                   "title": {"tag": "plain_text", "content": f"📈 AI 项目周趋势 · {date_str}"}},
        "elements": elements,
    }


def build(days: int | None = None, push: bool = False) -> dict:
    cfg = get_config().get("trend", {})
    days = days or cfg.get("window_days", 7)
    top_n = cfg.get("top_n", 8)
    date_str = today_str()

    payload = aggregate(iter_project_metas(), now().date(), days)
    write_json(trends_root() / f"{date_str}-weekly.json", payload)
    write_text(trends_root() / f"{date_str}-weekly.md", render_md(payload, date_str, top_n))
    log.info("已生成周趋势 trends/%s-weekly.(md|json)，窗口 %d 天，命中 %d 个项目",
             date_str, days, payload["total"])

    if push:
        from . import feishu_client
        feishu_client.send_card(_build_card(payload, date_str, top_n))
        log.info("周趋势已推送飞书。")
    return payload


def main():
    ap = argparse.ArgumentParser(description="AI 项目周趋势报告")
    ap.add_argument("--days", type=int, default=None, help="统计窗口天数（默认取 config）")
    ap.add_argument("--push", action="store_true", help="同时推送飞书")
    args = ap.parse_args()
    try:
        build(days=args.days, push=args.push)
    except Exception as e:
        log.exception("周趋势生成失败：%s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
