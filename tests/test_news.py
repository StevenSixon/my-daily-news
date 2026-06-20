"""AI 资讯轨：打分排序 / 截断 / Markdown 渲染（均不联网、不调 LLM）。"""
from src import build_summary, news_summary


def test_official_outranks_community_baseline():
    official = {"source_type": "official", "_ts": 0}
    community = {"source_type": "community", "_ts": 0, "points": 0}
    assert news_summary._score(official) > news_summary._score(community)


def test_recency_boosts_score(monkeypatch):
    import src.news_summary as ns

    class _Now:
        @staticmethod
        def timestamp():
            return 1_000_000.0

    monkeypatch.setattr(ns, "now", lambda: _Now())
    fresh = {"source_type": "paper", "_ts": 1_000_000.0}        # 当天
    stale = {"source_type": "paper", "_ts": 1_000_000.0 - 5 * 86400}  # 5 天前
    assert ns._score(fresh) > ns._score(stale)


def test_hn_points_bonus_is_capped():
    low = {"source_type": "community", "_ts": 0, "points": 80}
    high = {"source_type": "community", "_ts": 0, "points": 100_000}
    # 高赞有加成但被封顶，不会无限碾压
    assert news_summary._score(high) > news_summary._score(low)
    assert news_summary._score(high) - news_summary._score(low) <= 30


def test_summarize_caps_to_max_items(monkeypatch):
    monkeypatch.setattr(news_summary, "_cfg",
                        lambda: {"max_items": 3, "llm_summarize": False})
    cands = [
        {"title": f"t{i}", "url": f"https://x/{i}", "source": "S",
         "source_type": "paper", "_ts": float(i), "published": "2026-06-20"}
        for i in range(10)
    ]
    out = news_summary.summarize(cands)
    assert len(out) == 3
    # 内部排序键不应泄漏到产物
    assert all("_ts" not in it for it in out)


def test_render_news_includes_summary_and_link():
    news = [{
        "title": "Some title", "url": "https://e/x", "source": "OpenAI",
        "source_type": "official", "published": "2026-06-20",
        "summary_zh": "中文摘要", "category": "模型发布",
    }]
    md = "\n".join(build_summary._render_news(news))
    assert "## 📰 AI 资讯" in md
    assert "中文摘要" in md and "https://e/x" in md and "模型发布" in md


def test_render_news_empty_is_noop():
    assert build_summary._render_news([]) == []


def _news_section(card):
    for e in card.get("elements", []):
        c = e.get("text", {}).get("content", "") if e.get("tag") == "div" else ""
        if "📰 AI 资讯" in c:
            return c
    return None


def test_feishu_card_includes_news_section():
    from src import push
    payload = {
        "date": "2026-06-20", "count": 0, "items": [], "streaks": [],
        "news": [{
            "title": "T", "url": "https://e/x", "source": "OpenAI",
            "source_type": "official", "published": "2026-06-20",
            "summary_zh": "中文摘要", "category": "模型发布",
        }],
    }
    section = _news_section(push._build_card(payload))
    assert section is not None
    assert "中文摘要" in section and "https://e/x" in section and "模型发布" in section


def test_feishu_card_no_news_section_when_empty():
    from src import push
    payload = {"date": "2026-06-20", "count": 0, "items": [], "streaks": [], "news": []}
    assert _news_section(push._build_card(payload)) is None


def test_apply_quota_caps_per_type(monkeypatch):
    monkeypatch.setattr(news_summary, "_cfg",
                        lambda: {"type_quota": {"paper": 2}})
    items = (
        [{"source_type": "paper", "url": f"p{i}"} for i in range(5)]
        + [{"source_type": "official", "url": f"o{i}"} for i in range(3)]
    )
    out = news_summary._apply_quota(items)
    assert sum(1 for x in out if x["source_type"] == "paper") == 2     # 论文被限到 2
    assert sum(1 for x in out if x["source_type"] == "official") == 3  # 官方不限量


def test_per_source_max_caps_each_source(monkeypatch):
    monkeypatch.setattr(news_summary, "_cfg",
                        lambda: {"per_source_max": 2})
    items = (
        [{"source_type": "official", "source": "Claude", "url": f"c{i}"} for i in range(5)]
        + [{"source_type": "official", "source": "Anthropic", "url": f"a{i}"} for i in range(3)]
    )
    out = news_summary._apply_quota(items)
    assert sum(1 for x in out if x["source"] == "Claude") == 2
    assert sum(1 for x in out if x["source"] == "Anthropic") == 2


def test_get_with_retry_recovers_from_429(monkeypatch):
    import src.news_collect as nc

    class _Resp:
        def __init__(self, code):
            self.status_code = code
            self.headers = {"Retry-After": "0"}
            self.content = b"<rss></rss>"
        def raise_for_status(self):
            if self.status_code >= 400:
                raise RuntimeError(f"HTTP {self.status_code}")

    seq = [_Resp(429), _Resp(200)]
    monkeypatch.setattr(nc.time, "sleep", lambda *_: None)
    monkeypatch.setattr(nc.requests, "get", lambda *a, **k: seq.pop(0))
    r = nc._get_with_retry("http://x", retries=2)
    assert r.status_code == 200  # 首次 429 后重试拿到 200


def test_get_with_retry_raises_after_exhausted(monkeypatch):
    import src.news_collect as nc

    class _Resp:
        status_code = 429
        headers = {"Retry-After": "0"}
        def raise_for_status(self):
            raise RuntimeError("HTTP 429")

    monkeypatch.setattr(nc.time, "sleep", lambda *_: None)
    monkeypatch.setattr(nc.requests, "get", lambda *a, **k: _Resp())
    import pytest
    with pytest.raises(RuntimeError):
        nc._get_with_retry("http://x", retries=1)


def test_strip_gnews_suffix():
    from src.news_collect import _strip_gnews_suffix
    assert _strip_gnews_suffix("Claude Code now supports artifacts - Claude") == \
        "Claude Code now supports artifacts"
    assert _strip_gnews_suffix("Project Fetch: Phase two - Anthropic") == \
        "Project Fetch: Phase two"
    # 无尾巴时原样返回
    assert _strip_gnews_suffix("Plain title") == "Plain title"


def test_dedupe_by_event_keeps_first():
    items = [
        {"url": "a", "_event_key": "gpt5_release"},
        {"url": "b", "_event_key": "gpt5_release"},  # 同一事件 → 丢弃
        {"url": "c", "_event_key": ""},               # 空 key → 保留
        {"url": "d", "_event_key": ""},
        {"url": "e", "_event_key": "other"},
    ]
    out = news_summary._dedupe_by_event(items)
    urls = [x["url"] for x in out]
    assert urls == ["a", "c", "d", "e"]
