"""I-11a：why_worth_it + tags 在 analyze 规整、日报与飞书卡片渲染。"""
from src.analyze import _clean_tags
from src.build_summary import _render_md
from src.push import _build_card


def test_clean_tags_dedup_strip_and_cap():
    assert _clean_tags(["#Agent框架", "Agent框架", " 本地优先 ", "RAG", "TS", "多余"]) == \
        ["Agent框架", "本地优先", "RAG", "TS"]


def test_clean_tags_non_list():
    assert _clean_tags(None) == []
    assert _clean_tags("不是列表") == []


def _item(**kw):
    base = {"full_name": "o/r", "url": "https://github.com/o/r", "one_liner": "亮点",
            "language": "Python", "stars_total": 100, "stars_gained": 10,
            "is_new": True, "report_path": "../projects/o__r/analysis.md"}
    base.update(kw)
    return base


def test_daily_md_renders_why_and_tags():
    md = _render_md("2026-06-19", [_item(why_worth_it="解决 X，对后端有用", tags=["RAG", "自托管"])])
    assert "💡 值得看：解决 X，对后端有用" in md
    assert "`RAG`" in md and "`自托管`" in md


def test_daily_md_omits_when_absent():
    md = _render_md("2026-06-19", [_item()])  # 无 why/tags（老数据兼容）
    assert "值得看" not in md
    assert "🏷️" not in md


def test_card_renders_why_and_tags():
    payload = {"date": "2026-06-19", "count": 1,
               "items": [_item(why_worth_it="对独立开发者省时", tags=["CLI", "本地优先"])]}
    card = _build_card(payload)
    blob = str(card)
    assert "💡 对独立开发者省时" in blob
    # 卡片标签用中点分隔、无反引号（飞书 code chip 间距太窄会糊在一起）
    assert "🏷️ CLI · 本地优先" in blob
    assert "`CLI`" not in blob


def test_card_omits_when_absent():
    payload = {"date": "2026-06-19", "count": 1, "items": [_item()]}
    blob = str(_build_card(payload))
    assert "💡" not in blob
