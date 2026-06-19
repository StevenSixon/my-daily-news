"""GitHub 数据源：Trending 抓取 + REST Search/仓库详情。"""
from __future__ import annotations

import requests
from bs4 import BeautifulSoup

from .utils import parse_int

API = "https://api.github.com"
TRENDING = "https://github.com/trending"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ai-daily-news/1.0"


class GitHubClient:
    def __init__(self, token: str | None = None, timeout: int = 30):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {"Accept": "application/vnd.github+json", "User-Agent": UA}
        )
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

    # ---------- Trending（HTML 抓取，无官方 API）----------
    def trending(self, since: str = "daily", language: str = "") -> list[dict]:
        url = f"{TRENDING}/{language}".rstrip("/")
        resp = requests.get(
            url, params={"since": since}, headers={"User-Agent": UA}, timeout=self.timeout
        )
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        items: list[dict] = []
        for art in soup.select("article.Box-row"):
            link = art.select_one("h2 a")
            if not link:
                continue
            full_name = link.get("href", "").strip("/")
            if full_name.count("/") != 1:
                continue

            desc_el = art.select_one("p")
            description = desc_el.get_text(strip=True) if desc_el else ""

            lang_el = art.select_one('[itemprop="programmingLanguage"]')
            language_name = lang_el.get_text(strip=True) if lang_el else None

            star_el = art.select_one('a[href$="/stargazers"]')
            stars_total = parse_int(star_el.get_text()) if star_el else 0

            gained_el = art.select_one("span.d-inline-block.float-sm-right")
            stars_gained = parse_int(gained_el.get_text()) if gained_el else 0

            items.append(
                {
                    "full_name": full_name,
                    "url": f"https://github.com/{full_name}",
                    "description": description,
                    "language": language_name,
                    "stars_total": stars_total,
                    "stars_gained": stars_gained,
                    "period": since,
                    "topics": [],
                    "source": "trending",
                }
            )
        return items

    # ---------- Search API ----------
    def search(self, query: str, sort: str = "stars", order: str = "desc",
               per_page: int = 30) -> list[dict]:
        resp = self.session.get(
            f"{API}/search/repositories",
            params={"q": query, "sort": sort, "order": order, "per_page": per_page},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        out: list[dict] = []
        for r in resp.json().get("items", []):
            out.append(
                {
                    "full_name": r["full_name"],
                    "url": r["html_url"],
                    "description": r.get("description") or "",
                    "language": r.get("language"),
                    "stars_total": r.get("stargazers_count", 0),
                    "stars_gained": 0,  # Search API 无周增长，靠 rank_score 兜底排序
                    "created_at": (r.get("created_at") or "")[:10],
                    "period": "search",
                    "topics": r.get("topics", []),
                    "source": "search",
                }
            )
        return out

    # ---------- 仓库详情 ----------
    def repo(self, full_name: str) -> dict | None:
        resp = self.session.get(f"{API}/repos/{full_name}", timeout=self.timeout)
        if resp.status_code != 200:
            return None
        r = resp.json()
        return {
            "full_name": r["full_name"],
            "url": r["html_url"],
            "description": r.get("description") or "",
            "language": r.get("language"),
            "stars_total": r.get("stargazers_count", 0),
            "topics": r.get("topics", []),
            "license": (r.get("license") or {}).get("spdx_id"),
            "created_at": (r.get("created_at") or "")[:10],
            "pushed_at": (r.get("pushed_at") or "")[:10],
            "homepage": r.get("homepage"),
        }

    def readme(self, full_name: str) -> str:
        resp = self.session.get(
            f"{API}/repos/{full_name}/readme",
            headers={"Accept": "application/vnd.github.raw"},
            timeout=self.timeout,
        )
        return resp.text if resp.status_code == 200 else ""

    def latest_release(self, full_name: str) -> dict | None:
        resp = self.session.get(
            f"{API}/repos/{full_name}/releases/latest", timeout=self.timeout
        )
        if resp.status_code != 200:
            return None
        r = resp.json()
        return {
            "tag": r.get("tag_name"),
            "name": r.get("name"),
            "published_at": (r.get("published_at") or "")[:10],
            "body": (r.get("body") or "")[:2000],
        }

    def list_dir(self, full_name: str, path: str = "") -> list[str]:
        """列目录下的文件/子目录名（用于给 LLM 文档结构上下文）。"""
        resp = self.session.get(
            f"{API}/repos/{full_name}/contents/{path}", timeout=self.timeout
        )
        if resp.status_code != 200:
            return []
        data = resp.json()
        if not isinstance(data, list):
            return []
        return [item.get("name", "") for item in data]
