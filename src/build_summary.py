"""生成当天日报 daily/<date>.md（人读）+ daily/<date>.json（供 push 用）。"""
from __future__ import annotations

from .store import daily_root, write_json, write_text
from .utils import get_logger, today_str

log = get_logger()


def build(items: list[dict], streaks: list[dict] | None = None) -> dict:
    """items 为 analyze.learn() 返回的摘要条目列表；
    streaks 为「连续霸榜」榜单（同样来自 learn 返回值，纯展示）。"""
    date = today_str()
    streaks = streaks or []
    payload = {"date": date, "count": len(items), "items": items, "streaks": streaks}

    # JSON 侧车（push 读取，避免重复解析 md）
    write_json(daily_root() / f"{date}.json", payload)

    # 人读 Markdown
    write_text(daily_root() / f"{date}.md", _render_md(date, items, streaks))
    log.info("已生成日报 daily/%s.(md|json)，共 %d 个项目（霸榜 %d）",
             date, len(items), len(streaks))
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


def _render_md(date: str, items: list[dict], streaks: list[dict] | None = None) -> str:
    streaks = streaks or []
    lines = [f"# 🤖 AI 项目日报 · {date}", "", f"今日命中 **{len(items)}** 个 AI 应用项目。", ""]
    lines += _render_streaks(streaks)
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
