"""生成当天日报 daily/<date>.md（人读）+ daily/<date>.json（供 push 用）。"""
from __future__ import annotations

from .store import daily_root, write_json, write_text
from .utils import get_logger, today_str

log = get_logger()


def build(items: list[dict], streaks: list[dict] | None = None,
          news: list[dict] | None = None) -> dict:
    """items 为 analyze.learn() 返回的摘要条目列表；
    streaks 为「连续霸榜」榜单（同样来自 learn 返回值，纯展示）；
    news 为「AI 资讯」并行轨条目（来自 news_summary，可选）。"""
    date = today_str()
    streaks = streaks or []
    news = news or []
    # news 为附加字段：现有消费方（push.py / gen-data.mjs）只读 items，向后兼容。
    payload = {"date": date, "count": len(items), "items": items,
               "streaks": streaks, "news": news}

    # JSON 侧车（push 读取，避免重复解析 md）
    write_json(daily_root() / f"{date}.json", payload)

    # 人读 Markdown
    write_text(daily_root() / f"{date}.md", _render_md(date, items, streaks, news))
    log.info("已生成日报 daily/%s.(md|json)，共 %d 个项目（霸榜 %d，资讯 %d）",
             date, len(items), len(streaks), len(news))
    return payload


def _render_streaks(streaks: list[dict]) -> list[str]:
    """连续霸榜榜单（紧凑单行，纯展示，不含深度报告链接）。"""
    if not streaks:
        return []
    lines = ["## 🔥 连续霸榜", ""]
    for it in streaks:
        crown = " 🏆" if (it.get("streak_days") or 0) >= 7 else ""
        one = it.get("one_liner", "")
        lines.append(
            f"- **连续 {it.get('streak_days')} 天{crown}** ｜ "
            f"[{it['full_name']}]({it['url']}) ｜ "
            f"⭐ {it.get('stars_total')} (+{it.get('stars_gained', 0)})"
            + (f" ｜ {one}" if one else "")
        )
    lines.append("")
    return lines


_SOURCE_EMOJI = {"official": "🏢", "paper": "📄", "hf": "🤗", "community": "💬"}


def _render_news(news: list[dict]) -> list[str]:
    """AI 资讯段（并行轨，纯展示，按来源类型加 emoji）。"""
    if not news:
        return []
    lines = ["## 📰 AI 资讯", ""]
    for it in news:
        emoji = _SOURCE_EMOJI.get(it.get("source_type"), "🔗")
        cat = f"`{it['category']}` " if it.get("category") else ""
        desc = it.get("summary_zh") or it.get("title")
        meta = " ｜ ".join(x for x in (it.get("source"), it.get("published")) if x)
        lines.append(f"- {emoji} {cat}[{desc}]({it['url']})" + (f" ｜ {meta}" if meta else ""))
    lines.append("")
    return lines


def _render_md(date: str, items: list[dict], streaks: list[dict] | None = None,
               news: list[dict] | None = None) -> str:
    streaks = streaks or []
    news = news or []
    lines = [f"# 🤖 AI 项目日报 · {date}", "", f"今日命中 **{len(items)}** 个 AI 应用项目。", ""]
    lines += _render_streaks(streaks)
    lines += _render_news(news)
    if not items:
        lines.append("_今日无新增/更新项目。_")
        return "\n".join(lines)

    for i, it in enumerate(items, 1):
        badge = "🆕" if it.get("is_new") else f"🔥连续{it.get('streak_days')}天"
        lines += [
            f"## {i}. [{it['full_name']}]({it['url']}) {badge}",
            f"> {it.get('one_liner','')}",
            "",
        ]
        if it.get("why_worth_it"):
            lines.append(f"- 💡 值得看：{it['why_worth_it']}")
        if it.get("tags"):
            lines.append("- 🏷️ " + " ".join(f"`{t}`" for t in it["tags"]))
        if it.get("confidence") == "low":
            gaps = "；".join(it.get("info_gaps", [])[:2])
            lines.append("- ⚠️ 低置信，建议核对原文" + (f"（盲区：{gaps}）" if gaps else ""))
        lines += [
            f"- 语言：{it.get('language')} ｜ ⭐ {it.get('stars_total')} (+{it.get('stars_gained',0)})",
            f"- 深度报告：[`{it['report_path']}`]({it['report_path']})",
            "",
        ]
    return "\n".join(lines)
