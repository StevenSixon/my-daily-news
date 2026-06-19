"""I-11b：周趋势聚合（纯函数）+ 渲染。"""
from datetime import date

from src.trend import _to_date, _weekly_gain, aggregate, render_md

TODAY = date(2026, 6, 19)


def _meta(name, apps, first_seen, streak=1, **kw):
    base = {"full_name": name, "url": f"https://github.com/{name}",
            "one_liner": f"{name} 亮点", "tags": [], "language": "Python",
            "first_seen": first_seen, "streak_days": streak, "appearances": apps}
    base.update(kw)
    return base


def test_to_date_parsing():
    assert _to_date("2026-06-19") == date(2026, 6, 19)
    assert _to_date("bad") is None
    assert _to_date(None) is None


def test_weekly_gain_uses_delta_when_multiple_points():
    apps = [{"date": "2026-06-14", "stars_total": 1000, "stars_gained": 50},
            {"date": "2026-06-18", "stars_total": 1800, "stars_gained": 0}]
    assert _weekly_gain(apps) == 800  # 1800 - 1000


def test_weekly_gain_single_point_falls_back_to_gained():
    apps = [{"date": "2026-06-18", "stars_total": 5000, "stars_gained": 1500}]
    assert _weekly_gain(apps) == 1500


def test_aggregate_filters_window_and_ranks():
    metas = [
        # 窗口内多次出现、增量大、但首见在窗口外 → 最热 + 持续上榜（非新晋）
        _meta("a/hot", [
            {"date": "2026-06-14", "stars_total": 1000, "stars_gained": 100},
            {"date": "2026-06-18", "stars_total": 3000, "stars_gained": 200},
        ], first_seen="2026-06-05", streak=4),
        # 窗口内、单次、新晋
        _meta("b/new", [
            {"date": "2026-06-19", "stars_total": 800, "stars_gained": 800},
        ], first_seen="2026-06-19"),
        # 窗口外（早于 6-12）→ 应被过滤
        _meta("c/old", [
            {"date": "2026-06-01", "stars_total": 9000, "stars_gained": 50},
        ], first_seen="2026-05-01"),
    ]
    p = aggregate(metas, TODAY, days=7)
    assert p["total"] == 2  # c/old 被过滤
    assert p["hottest"][0]["full_name"] == "a/hot"     # +2000 最大
    assert [r["full_name"] for r in p["rising"]] == ["a/hot"]  # 仅 a/hot 出现 >=2 天
    assert [r["full_name"] for r in p["newcomers"]] == ["b/new"]


def test_aggregate_empty():
    p = aggregate([], TODAY, days=7)
    assert p == {"window_days": 7, "total": 0, "hottest": [], "rising": [], "newcomers": []}


def test_render_md_contains_sections():
    metas = [_meta("a/hot", [
        {"date": "2026-06-18", "stars_total": 3000, "stars_gained": 200}],
        first_seen="2026-06-18", why_worth_it="解决 X")]
    md = render_md(aggregate(metas, TODAY, 7), "2026-06-19", top_n=8)
    assert "本周最热" in md and "持续上榜" in md and "本周新晋" in md
    assert "a/hot" in md
