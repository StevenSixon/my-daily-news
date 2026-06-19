"""_rank_score 排序键（I-2 回归：Search 源不再恒为 0）。"""
from src.collect import _rank_score


def test_trending_uses_real_gain():
    item = {"full_name": "x/y", "stars_gained": 500, "stars_total": 9000}
    assert _rank_score(item, {}) == 500


def test_search_with_history_uses_delta():
    index = {"a/b": {"last_stars_total": 1000}}
    item = {"full_name": "a/b", "stars_gained": 0, "stars_total": 1300}
    assert _rank_score(item, index) == 300


def test_search_history_delta_never_negative():
    index = {"a/b": {"last_stars_total": 2000}}
    item = {"full_name": "a/b", "stars_gained": 0, "stars_total": 1800}
    assert _rank_score(item, index) == 0


def test_new_search_item_uses_velocity(monkeypatch):
    # 固定"今天"，避免依赖真实日期
    import datetime as _dt
    import src.collect as collect

    class _FixedNow:
        @staticmethod
        def date():
            return _dt.date(2026, 6, 19)

    monkeypatch.setattr(collect, "now", lambda: _FixedNow())
    item = {"full_name": "c/d", "stars_gained": 0, "stars_total": 3000,
            "created_at": "2026-05-20"}  # 30 天前
    assert _rank_score(item, {}) == 100  # 3000 / 30


def test_new_search_item_no_date_is_zero():
    item = {"full_name": "e/f", "stars_gained": 0, "stars_total": 3000}
    assert _rank_score(item, {}) == 0


def test_bad_created_at_does_not_crash():
    item = {"full_name": "e/f", "stars_gained": 0, "stars_total": 3000,
            "created_at": "not-a-date"}
    assert _rank_score(item, {}) == 0
