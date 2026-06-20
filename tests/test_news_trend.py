"""周资讯回顾聚合（纯函数，不联网）。"""
from datetime import date

from src.news_trend import aggregate

TODAY = date(2026, 6, 20)


def _daily(d, news):
    return {"date": d, "news": news}


def test_window_excludes_old_editions():
    dailies = [
        _daily("2026-06-20", [{"url": "u1", "category": "研究", "source": "A"}]),
        _daily("2026-06-01", [{"url": "u2", "category": "研究", "source": "B"}]),  # 窗口外
    ]
    out = aggregate(dailies, TODAY, days=7)
    assert out["total"] == 1
    urls = [r["url"] for rows in out["by_category"].values() for r in rows]
    assert urls == ["u1"]


def test_dedupe_same_url_across_editions():
    dailies = [
        _daily("2026-06-20", [{"url": "dup", "category": "产品", "source": "A"}]),
        _daily("2026-06-19", [{"url": "dup", "category": "产品", "source": "A"}]),
    ]
    out = aggregate(dailies, TODAY, days=7)
    assert out["total"] == 1


def test_grouped_by_category_in_order():
    dailies = [_daily("2026-06-20", [
        {"url": "a", "category": "观点", "source": "S", "source_type": "community"},
        {"url": "b", "category": "模型发布", "source": "S", "source_type": "official"},
    ])]
    out = aggregate(dailies, TODAY, days=7)
    # _CAT_ORDER 把「模型发布」排在「观点」之前
    assert list(out["by_category"].keys()) == ["模型发布", "观点"]
    assert out["source_counts"] == {"S": 2}


def test_empty_window_is_zero():
    out = aggregate([], TODAY, days=7)
    assert out["total"] == 0
    assert out["by_category"] == {}
