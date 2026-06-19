"""LLM JSON 容错：去围栏 / 抽 JSON 块 / 解析修复。"""
from src.llm_client import _find_json_block, _strip_fences, _try_parse_json


def test_strip_fences_plain():
    assert _strip_fences('{"a":1}') == '{"a":1}'


def test_strip_fences_json_fence():
    text = '```json\n{"a": 1}\n```'
    assert _strip_fences(text).strip() == '{"a": 1}'


def test_strip_fences_bare_fence():
    text = '```\n{"a": 1}\n```'
    assert _strip_fences(text).strip() == '{"a": 1}'


def test_find_json_block_skips_preamble():
    text = 'Sure, here is the JSON:\n{"a": 1}'
    assert _find_json_block(text).startswith("{")


def test_try_parse_clean():
    assert _try_parse_json('{"a": 1}') == {"a": 1}


def test_try_parse_with_fence_and_preamble():
    text = 'Here you go:\n```json\n{"keep": true}\n```'
    assert _try_parse_json(text) == {"keep": True}


def test_try_parse_trailing_comma_repaired():
    assert _try_parse_json('{"a": 1, "b": [1, 2,],}') == {"a": 1, "b": [1, 2]}


def test_try_parse_invalid_returns_none():
    assert _try_parse_json("not json at all") is None


def test_find_json_block_drops_trailing_junk():
    # JSON 后还有多余文字时，只取配对完整的那一段
    assert _find_json_block('{"a": 1}\n以上就是结果。') == '{"a": 1}'


def test_find_json_block_ignores_braces_in_strings():
    text = '{"msg": "use {curly} and [square] here"}'
    assert _find_json_block(text) == text
    assert _try_parse_json(text) == {"msg": "use {curly} and [square] here"}
