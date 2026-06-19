"""读取当天日报 JSON → 构建飞书交互卡片 → 私聊推送（含重试）。"""
from __future__ import annotations

import sys
import time

from . import feishu_client
from .config_loader import get_config
from .store import daily_root, read_json
from .utils import get_logger, today_str

log = get_logger()


def _build_card(payload: dict) -> dict:
    cfg = get_config()["feishu"]
    top_n = cfg.get("card_top_n", 5)
    date = payload["date"]
    items = payload.get("items", [])[:top_n]
    total = payload.get("count", 0)

    elements: list[dict] = []
    if not items:
        elements.append({"tag": "div", "text": {"tag": "lark_md", "content": "今日无新增/更新项目。"}})
    else:
        for i, it in enumerate(items, 1):
            badge = "🆕" if it.get("is_new") else f"🔥连续{it.get('streak_days')}天"
            content = (
                f"**{i}. [{it['full_name']}]({it['url']})** {badge}\n"
                f"{it.get('one_liner','')}\n"
                f"语言 {it.get('language')} ｜ ⭐ {it.get('stars_total')} (+{it.get('stars_gained',0)})"
            )
            elements.append({"tag": "div", "text": {"tag": "lark_md", "content": content}})
            elements.append({"tag": "hr"})

    elements.append({
        "tag": "note",
        "elements": [{"tag": "lark_md",
                      "content": f"📂 详细报告见本地项目库 projects/ ｜ 今日命中 {total} 个"}],
    })

    return {
        "config": {"wide_screen_mode": True},
        "header": {
            "template": cfg.get("header_template", "blue"),
            "title": {"tag": "plain_text", "content": f"🤖 AI 项目日报 · {date}"},
        },
        "elements": elements,
    }


def push(date: str | None = None, retries: int = 2) -> None:
    date = date or today_str()
    payload = read_json(daily_root() / f"{date}.json")
    if payload is None:
        log.error("找不到 daily/%s.json，请先运行 pipeline。", date)
        sys.exit(1)

    card = _build_card(payload)
    for attempt in range(retries + 1):
        try:
            feishu_client.send_card(card)
            return
        except Exception as e:
            log.warning("推送失败（第 %d 次）：%s", attempt + 1, e)
            if attempt < retries:
                time.sleep(2 * (attempt + 1))
    log.error("飞书推送最终失败。")
    sys.exit(1)


if __name__ == "__main__":
    push(sys.argv[1] if len(sys.argv) > 1 else None)
