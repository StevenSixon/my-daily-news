"""周资讯回顾报告（二次报告）。

聚合统计窗口内各日 daily/<date>.json 的 `news` 字段，按分类 / 来源汇总成
一份「本周 AI 资讯回顾」，写入 trends/<date>-news-weekly.(md|json)，可选推送飞书。
数据全部来自已落盘的日报，无需再抓取/调 LLM。
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from datetime import date, timedelta

from .config_loader import get_config
from .store import daily_root, read_json, trends_root, write_json, write_text
from .utils import get_logger, now, today_str

log = get_logger()

# 与日报/看板一致的来源类型 emoji
_TYPE_EMOJI = {"official": "🏢", "paper": "📄", "hf": "🤗", "community": "💬"}
# 分类展示顺序
_CAT_ORDER = ["模型发布", "产品", "研究", "工程", "融资/商业", "观点", "其他"]


def _to_date(s) -> date | None:
    try:
        y, m, d = (int(x) for x in str(s).split("-"))
        return date(y, m, d)
    except (ValueError, TypeError, AttributeError):
        return None


def aggregate(dailies: list[dict], today: date, days: int = 7) -> dict:
    """把窗口内各日 news 聚合成周回顾。纯函数，便于测试。

    dailies：各日 daily payload（含 date + news）。跨日按 URL 去重。"""
    window_start = today - timedelta(days=days)
    seen: set[str] = set()
    items: list[dict] = []
    for d in dailies:
        ddate = _to_date(d.get("date"))
        if not ddate or ddate <= window_start:
            continue
        for n in d.get("news", []) or []:
            url = n.get("url")
            if not url or url in seen:
                continue
            seen.add(url)
            items.append({
                "title": n.get("title", ""),
                "url": url,
                "source": n.get("source", ""),
                "source_type": n.get("source_type", ""),
                "published": n.get("published", ""),
                "summary_zh": n.get("summary_zh", ""),
                "category": n.get("category") or "其他",
                "edition": d.get("date", ""),
            })

    # 按分类分组（组内按发布日期倒序），分类按 _CAT_ORDER 排列
    by_cat: dict[str, list[dict]] = {}
    for it in items:
        by_cat.setdefault(it["category"], []).append(it)
    for rows in by_cat.values():
        rows.sort(key=lambda r: r.get("published", ""), reverse=True)
    categories = [c for c in _CAT_ORDER if c in by_cat] + \
                 [c for c in by_cat if c not in _CAT_ORDER]

    return {
        "window_days": days,
        "total": len(items),
        "by_category": {c: by_cat[c] for c in categories},
        "source_counts": dict(Counter(it["source"] for it in items).most_common()),
        "type_counts": dict(Counter(it["source_type"] for it in items)),
    }


def render_md(payload: dict, date_str: str, top_n: int) -> str:
    days = payload["window_days"]
    lines = [f"# 📰 AI 资讯周回顾 · 截至 {date_str}", "",
             f"近 **{days}** 天共收录 **{payload['total']}** 条 AI 资讯。", ""]

    if payload["source_counts"]:
        srcs = " ｜ ".join(f"{s} {c}" for s, c in list(payload["source_counts"].items())[:8])
        lines += [f"**来源分布**：{srcs}", ""]

    if payload["total"] == 0:
        lines.append("_本周无资讯。_")
        return "\n".join(lines)

    for cat, rows in payload["by_category"].items():
        lines.append(f"## {cat}（{len(rows)}）")
        for r in rows[:top_n]:
            emoji = _TYPE_EMOJI.get(r["source_type"], "🔗")
            desc = r.get("summary_zh") or r.get("title")
            meta = " ｜ ".join(x for x in (r.get("source"), r.get("published")) if x)
            lines.append(f"- {emoji} [{desc}]({r['url']})" + (f" ｜ {meta}" if meta else ""))
        if len(rows) > top_n:
            lines.append(f"  - …另有 {len(rows) - top_n} 条")
        lines.append("")
    return "\n".join(lines)


def _build_card(payload: dict, date_str: str, top_n: int) -> dict:
    elements: list[dict] = []
    if payload["total"] == 0:
        elements.append({"tag": "div", "text": {"tag": "lark_md", "content": "本周无资讯。"}})
    else:
        for cat, rows in payload["by_category"].items():
            body = [f"**{cat}（{len(rows)}）**"]
            for r in rows[:top_n]:
                emoji = _TYPE_EMOJI.get(r["source_type"], "🔗")
                desc = r.get("summary_zh") or r.get("title")
                body.append(f"{emoji} [{desc}]({r['url']})")
            elements.append({"tag": "div", "text": {"tag": "lark_md", "content": "\n".join(body)}})
            elements.append({"tag": "hr"})
    elements.append({"tag": "note", "elements": [
        {"tag": "lark_md", "content": f"📰 近 {payload['window_days']} 天收录 {payload['total']} 条资讯"}]})

    return {
        "config": {"wide_screen_mode": True},
        "header": {"template": "turquoise",
                   "title": {"tag": "plain_text", "content": f"📰 AI 资讯周回顾 · {date_str}"}},
        "elements": elements,
    }


def _load_window_dailies(today: date, days: int) -> list[dict]:
    """读取窗口内（含今天回溯 days 天）存在的 daily/<date>.json。"""
    out: list[dict] = []
    for i in range(days + 1):
        d = today - timedelta(days=i)
        payload = read_json(daily_root() / f"{d.isoformat()}.json")
        if payload:
            out.append(payload)
    return out


def build(days: int | None = None, push: bool = False) -> dict:
    cfg = get_config().get("news_trend", {})
    days = days or cfg.get("window_days", 7)
    top_n = cfg.get("top_n", 8)
    date_str = today_str()

    dailies = _load_window_dailies(now().date(), days)
    payload = aggregate(dailies, now().date(), days)
    write_json(trends_root() / f"{date_str}-news-weekly.json", payload)
    write_text(trends_root() / f"{date_str}-news-weekly.md", render_md(payload, date_str, top_n))
    log.info("已生成资讯周回顾 trends/%s-news-weekly.(md|json)，窗口 %d 天，收录 %d 条",
             date_str, days, payload["total"])

    if push and payload["total"] > 0:
        from . import feishu_client
        feishu_client.send_card(_build_card(payload, date_str, top_n))
        log.info("资讯周回顾已推送飞书。")
    return payload


def main():
    ap = argparse.ArgumentParser(description="AI 资讯周回顾报告")
    ap.add_argument("--days", type=int, default=None, help="统计窗口天数（默认取 config）")
    ap.add_argument("--push", action="store_true", help="同时推送飞书")
    args = ap.parse_args()
    try:
        build(days=args.days, push=args.push)
    except Exception as e:
        log.exception("资讯周回顾生成失败：%s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
