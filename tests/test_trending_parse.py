"""Trending HTML 解析回归。

用一份真实抓取并裁剪的 fixture（tests/fixtures/trending_daily.html）。
GitHub 改版导致选择器失效时，这些断言会第一时间报警。
"""
from pathlib import Path

import pytest

from src.github_client import GitHubClient

FIXTURE = Path(__file__).parent / "fixtures" / "trending_daily.html"


class _FakeResp:
    def __init__(self, text):
        self.text = text
        self.status_code = 200

    def raise_for_status(self):
        pass


@pytest.fixture
def parsed():
    html = FIXTURE.read_text(encoding="utf-8")
    gh = GitHubClient(token="x")
    gh.session.get = lambda *a, **k: _FakeResp(html)
    return gh.trending(since="daily")


def test_parses_all_rows(parsed):
    assert len(parsed) == 3


def test_first_repo_full_name(parsed):
    assert parsed[0]["full_name"] == "DeusData/codebase-memory-mcp"


def test_every_item_has_valid_shape(parsed):
    for it in parsed:
        assert it["full_name"].count("/") == 1
        assert it["source"] == "trending"
        assert it["url"] == f"https://github.com/{it['full_name']}"
        assert isinstance(it["stars_total"], int) and it["stars_total"] > 0
        assert isinstance(it["stars_gained"], int) and it["stars_gained"] > 0
        assert it["period"] == "daily"


def test_language_extracted(parsed):
    langs = {it["full_name"]: it["language"] for it in parsed}
    assert langs["google-research/timesfm"] == "Python"
