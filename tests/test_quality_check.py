"""I-11 质量自检：确定性闸门 + 有效置信度 + 脚注 + 低置信渲染。"""
from src.analyze import (_clean_str_list, _effective_confidence,
                         _quality_flags, _quality_footer)
from src.build_summary import _render_md
from src.push import _build_card

_GOOD = ("## 它是什么\nX。\n## 为什么火\nY。\n## 技术栈\nZ。\n"
         "## 核心能力\nA。\n## 适用场景\nB。\n## 同类对比\nC。\n## 版本动态\nD。" + "补充说明 " * 30)


def test_clean_str_list_dedup_cap():
    assert _clean_str_list(["a", "a", " b ", "c", "d", "e", "f"], 5) == ["a", "b", "c", "d", "e"]
    assert _clean_str_list(None, 5) == []


def test_quality_flags_clean_report_has_none():
    report = {"analysis_md": _GOOD, "one_liner": "亮点", "quickstart_md": "装一下"}
    assert _quality_flags(report) == []


def test_quality_flags_detects_short_and_missing_sections():
    report = {"analysis_md": "## 它是什么\n太短了", "one_liner": "", "quickstart_md": ""}
    flags = _quality_flags(report)
    assert any("过短" in f for f in flags)
    assert any("缺小标题" in f for f in flags)
    assert "缺一句话亮点" in flags
    assert "缺上手指南" in flags


def test_effective_confidence_downgrades_on_flags():
    assert _effective_confidence("high", []) == "high"
    assert _effective_confidence("high", ["报告过短"]) == "medium"
    assert _effective_confidence("medium", ["x"]) == "low"
    assert _effective_confidence("low", ["x"]) == "low"          # 不低于 low
    assert _effective_confidence("garbage", []) == "medium"      # 非法值兜底
    assert _effective_confidence(None, []) == "medium"


def test_quality_footer_contains_confidence_and_gaps():
    f = _quality_footer("low", ["无 benchmark"], ["报告过短"])
    assert "置信度：**low**" in f
    assert "无 benchmark" in f
    assert "报告过短" in f


def _item(**kw):
    base = {"full_name": "o/r", "url": "https://github.com/o/r", "one_liner": "亮点",
            "language": "Python", "stars_total": 100, "stars_gained": 10,
            "is_new": True, "report_path": "../projects/o__r/analysis.md"}
    base.update(kw)
    return base


def test_daily_md_shows_low_confidence_warning():
    md = _render_md("2026-06-19", [_item(confidence="low", info_gaps=["无部署说明", "无 benchmark"])])
    assert "⚠️ 低置信" in md
    assert "无部署说明" in md


def test_daily_md_no_warning_when_high():
    md = _render_md("2026-06-19", [_item(confidence="high")])
    assert "低置信" not in md


def test_card_shows_low_confidence_warning():
    payload = {"date": "2026-06-19", "count": 1, "items": [_item(confidence="low")]}
    assert "⚠️ 低置信" in str(_build_card(payload))
