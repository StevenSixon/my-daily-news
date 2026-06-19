"""关键词分类整词匹配（I-1 回归：避免 hawaii/air/storage/iptv 误命中）。"""
import pytest

from src.collect import _KW_RE, _classify_ai_keyword


@pytest.mark.parametrize("text", [
    "AI agent for code",
    "fine-tuning toolkit",
    "fine-tune your model",
    "a rag pipeline",
    "model context protocol server",
    "an LLM chatbot",
    "multimodal embedding search",
])
def test_keyword_hits(text):
    assert _KW_RE.search(text.lower())


@pytest.mark.parametrize("text", [
    "visit hawaii travel guide",   # 'ai' 子串不应命中
    "fresh air quality sensor",    # 'air' 不应命中 'ai'
    "storage drag and drop",       # 'rag' 子串不应命中
    "iptv channel list m3u",       # 真实误判案例
    "a simple todo app",
])
def test_keyword_non_hits(text):
    assert not _KW_RE.search(text.lower())


def test_classify_excludes_list_like():
    c = {"full_name": "x/awesome-ai", "description": "awesome AI list", "topics": []}
    v = _classify_ai_keyword(c)
    assert v["keep"] is False
    assert "列表" in v["reason"] or "教程" in v["reason"]


def test_classify_iptv_rejected():
    c = {"full_name": "iptv-org/iptv",
         "description": "Collection of publicly available IPTV channels",
         "topics": ["iptv", "m3u", "playlist", "tv"]}
    assert _classify_ai_keyword(c)["keep"] is False


def test_classify_ai_app_kept():
    c = {"full_name": "foo/ai-agent",
         "description": "An AI agent that writes code",
         "topics": ["llm", "agent"]}
    v = _classify_ai_keyword(c)
    assert v["keep"] is True
    assert v["category"] == "AI 应用"
