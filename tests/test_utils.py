"""parse_int / repo_slug 等纯函数。"""
from src.utils import parse_int, repo_slug


def test_parse_int_extracts_digits():
    assert parse_int("1,234 stars today") == 1234
    assert parse_int("749") == 749
    assert parse_int("⭐ 7,711") == 7711


def test_parse_int_no_digits_returns_zero():
    assert parse_int("") == 0
    assert parse_int(None) == 0
    assert parse_int("stars") == 0


def test_repo_slug():
    assert repo_slug("owner/repo") == "owner__repo"
    assert repo_slug("a/b") == "a__b"
