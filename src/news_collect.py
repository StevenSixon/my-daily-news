"""资讯采集（与项目采集 collect.py 并行的独立轨）。

RSS（官方博客 / 论文 / HF）+ Hacker News API → 时间窗过滤 → 按 URL 去重
→ AI 相关性过滤。产出文章条目（不进项目榜），交给 news_summary 做 LLM 摘要/分类。

不引入任何密钥：全部为公开 RSS / 公共 API。失效源会被安全跳过，不影响其余源。
"""
from __future__ import annotations

import re
import time
from calendar import timegm

import feedparser
import requests

from .config_loader import get_config
from .store import ROOT, read_json, write_json
from .utils import get_logger, now

log = get_logger()

SEEN_PATH = ROOT / "data" / "news-seen.json"  # {url: 首次见到日期}
_UA = {"User-Agent": "Mozilla/5.0 (compatible; ai-daily-news/1.0)"}
_HN_API = "https://hn.algolia.com/api/v1/search_by_date"

# 社区源（如 HN）才需要的 AI 相关性过滤；官方/论文源默认相关。
_AI_RE = re.compile(
    r"\b(ai|a\.i\.|llm|gpt|agent|rag|chatbot|prompt|diffusion|generative|openai|"
    r"anthropic|claude|gemini|llama|mistral|deepseek|qwen|kimi|grok|embedding|"
    r"transformer|multimodal|copilot|inference|fine-tun|neural net|"
    r"machine learning|deep learning|model)\b",
    re.I,
)


def _cfg() -> dict:
    return get_config().get("news", {}) or {}


def _cutoff_ts(days: int) -> float:
    """时间窗下界（unix 秒）。只保留窗口内发布的条目，避免首跑回灌历史。"""
    return now().timestamp() - days * 86400


def _entry_ts(entry) -> float | None:
    """从 feed 条目解析发布时间（unix 秒）；缺失返回 None。"""
    for key in ("published_parsed", "updated_parsed"):
        t = entry.get(key)
        if t:
            try:
                return float(timegm(t))  # struct_time 视为 UTC
            except (TypeError, ValueError, OverflowError):
                pass
    return None


def _ts_to_date(ts: float) -> str:
    from datetime import datetime, timezone
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")


def _clean(text: str) -> str:
    """去标签 + 压空白，取纯文本摘要片段。"""
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _strip_gnews_suffix(title: str) -> str:
    """Google News 标题尾部会附「 - 来源名」（如 "… - Anthropic"），去掉它。"""
    return re.sub(r"\s+-\s+[^-]+$", "", title).strip() or title


def _fetch_rss(name: str, url: str, source_type: str, cutoff: float,
               ai_filter: bool = False) -> list[dict]:
    """抓取并解析一个 RSS/Atom 源。ai_filter=True 时（社区论坛源）按关键词过滤标题。"""
    out: list[dict] = []
    try:
        r = requests.get(url, headers=_UA, timeout=15)
        r.raise_for_status()
        feed = feedparser.parse(r.content)
    except Exception as e:
        log.warning("资讯源 %s 抓取失败：%s", name, e)
        return out
    if feed.bozo and not feed.entries:
        log.warning("资讯源 %s 解析为空（可能非标准 feed）", name)
        return out
    is_gnews = "news.google.com" in url
    for e in feed.entries:
        link = (e.get("link") or "").strip()
        title = _clean(e.get("title", ""))
        if is_gnews:
            title = _strip_gnews_suffix(title)
        if not link or not title:
            continue
        if ai_filter and not _AI_RE.search(title):
            continue
        ts = _entry_ts(e)
        if ts is None or ts < cutoff:
            continue  # 无时间或超出窗口
        out.append({
            "title": title,
            "url": link,
            "source": name,
            "source_type": source_type,
            "published": _ts_to_date(ts),
            "_ts": ts,
            "summary_raw": _clean(e.get("summary", ""))[:400],
        })
    log.info("资讯源 %s：窗口内 %d 条", name, len(out))
    return out


def _fetch_hn(cutoff: float) -> list[dict]:
    """Hacker News（Algolia API）：取窗口内、点赞达标的 story，再按 AI 关键词过滤。"""
    cfg = _cfg()
    min_points = int(cfg.get("hn_min_points", 80))
    out: list[dict] = []
    try:
        r = requests.get(
            _HN_API,
            params={
                "tags": "story",
                "numericFilters": f"points>={min_points},created_at_i>{int(cutoff)}",
                "hitsPerPage": 60,
            },
            headers=_UA, timeout=15,
        )
        r.raise_for_status()
        hits = r.json().get("hits", [])
    except Exception as e:
        log.warning("资讯源 Hacker News 抓取失败：%s", e)
        return out
    for h in hits:
        title = _clean(h.get("title") or "")
        # HN 故事可能无外链（Ask HN 等）→ 回退到 HN 讨论页
        link = (h.get("url") or "").strip() or f"https://news.ycombinator.com/item?id={h.get('objectID')}"
        if not title or not _AI_RE.search(title):
            continue
        ts = float(h.get("created_at_i") or 0)
        out.append({
            "title": title,
            "url": link,
            "source": "Hacker News",
            "source_type": "community",
            "published": _ts_to_date(ts) if ts else "",
            "_ts": ts,
            "points": int(h.get("points") or 0),
            "summary_raw": "",
        })
    log.info("资讯源 Hacker News：AI 相关 %d 条（points≥%d）", len(out), min_points)
    return out


def load_seen() -> dict:
    return read_json(SEEN_PATH) or {}


def mark_seen(items: list[dict]) -> None:
    """把已采纳的资讯 URL 写入 seen，避免后续重复出现。同时清理超窗的旧记录。"""
    seen = load_seen()
    today = now().strftime("%Y-%m-%d")
    for it in items:
        seen[it["url"]] = today
    # 清理：只保留近 30 天的去重记录，控制文件体积
    cutoff = _cutoff_ts(30)
    kept = {}
    for url, d in seen.items():
        try:
            y, m, dd = (int(x) for x in d.split("-"))
            from datetime import datetime, timezone
            if datetime(y, m, dd, tzinfo=timezone.utc).timestamp() >= cutoff:
                kept[url] = d
        except (ValueError, TypeError):
            kept[url] = d
    write_json(SEEN_PATH, kept)


def collect_news() -> list[dict]:
    """返回去重后的资讯候选（未排序、未摘要）。news.enabled=false 时返回 []。"""
    cfg = _cfg()
    if not cfg.get("enabled", False):
        return []

    window = int(cfg.get("window_days", 3))
    cutoff = _cutoff_ts(window)
    sources = cfg.get("sources", {}) or {}

    raw: list[dict] = []
    for source_type in ("official", "paper", "hf"):
        for s in sources.get(source_type, []) or []:
            url = s.get("url")
            if not url:
                continue
            raw += _fetch_rss(s.get("name", url), url, source_type, cutoff)

    # Reddit：JSON API 已被反爬封禁，改用 RSS 端点；按 AI 关键词过滤标题。
    # Reddit 对密集请求会 429，源间留短延时（首个不延时）。
    reddit_srcs = sources.get("reddit", []) or []
    for i, s in enumerate(reddit_srcs):
        url = s.get("url")
        if not url:
            continue
        if i > 0:
            time.sleep(2)
        raw += _fetch_rss(s.get("name", url), url, "community", cutoff, ai_filter=True)

    if cfg.get("hacker_news", True):
        raw += _fetch_hn(cutoff)

    # 批内按 URL 去重（多源可能撞同一链接）
    by_url: dict[str, dict] = {}
    for it in raw:
        by_url.setdefault(it["url"], it)

    # 过滤掉历史已收录的 URL
    seen = load_seen()
    fresh = [it for it in by_url.values() if it["url"] not in seen]

    log.info("资讯：原始 %d → 去重 %d → 未收录 %d（窗口 %d 天）",
             len(raw), len(by_url), len(fresh), window)
    return fresh


if __name__ == "__main__":
    for it in collect_news():
        print(f'[{it["source_type"]:9}] {it["source"]:14} {it["published"]} | {it["title"][:70]}')
