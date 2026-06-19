"""采集：Trending + Search 双源 → 合并 → AI 应用过滤 → 去重/复访判定。"""
from __future__ import annotations

import re
from datetime import date, timedelta

from . import llm_client
from .config_loader import env, get_config
from .github_client import GitHubClient
from .store import CLASSIFY_LOG, append_jsonl, load_index
from .utils import get_logger, now, today_str

log = get_logger()

# 无 LLM 时的兜底关键词过滤（整词匹配，避免 "ai" 命中 hawaii/air 之类）
_AI_KEYWORDS = [
    "ai", "llm", "gpt", "agent", "rag", "chatbot", "prompt", "diffusion",
    "generative", "openai", "anthropic", "claude", "embedding", "transformer",
    "multimodal", "copilot", "vector", "inference", "model context",
]
# 前缀型关键词：只卡左边界，匹配 fine-tune / fine-tuning 等变体
_AI_PREFIXES = ["fine-tun"]
_EXCLUDE_HINTS = ["awesome", "papers", "paper list", "course", "tutorial", "book", "cheatsheet"]

_KW_RE = re.compile(
    "|".join([rf"\b{re.escape(k)}\b" for k in _AI_KEYWORDS]
             + [rf"\b{re.escape(p)}" for p in _AI_PREFIXES])
)


def _client() -> GitHubClient:
    return GitHubClient(token=env("GITHUB_TOKEN"))


def _gather(gh: GitHubClient) -> dict[str, dict]:
    """抓取双源并按 full_name 合并；保留最大 stars_gained。"""
    cfg = get_config()
    focus = cfg["focus"]
    coll = cfg["collect"]
    merged: dict[str, dict] = {}

    def absorb(item: dict):
        key = item["full_name"]
        if key in merged:
            cur = merged[key]
            cur["stars_gained"] = max(cur["stars_gained"], item["stars_gained"])
            cur["topics"] = list({*cur.get("topics", []), *item.get("topics", [])})
            if not cur.get("created_at") and item.get("created_at"):
                cur["created_at"] = item["created_at"]
            if item["source"] not in cur["source"]:
                cur["source"] += f"+{item['source']}"
        else:
            merged[key] = dict(item)

    # 数据源 A：Trending
    if "trending" in coll["sources"]:
        for since in coll.get("trending_since", ["daily"]):
            try:
                for it in gh.trending(since=since):
                    absorb(it)
            except Exception as e:
                log.warning("Trending(%s) 抓取失败：%s", since, e)

    # 数据源 B：Search（逐 topic 搜索后合并，实现 topic 的 OR）
    if "search" in coll["sources"]:
        created_after = (now() - timedelta(days=focus["created_within_days"])).strftime("%Y-%m-%d")
        for topic in focus["search_topics"]:
            q = (f"topic:{topic} stars:>={focus['min_stars']} "
                 f"created:>={created_after} pushed:>={_pushed_after(focus)}")
            try:
                for it in gh.search(q, per_page=coll.get("per_topic_limit", 20)):
                    absorb(it)
            except Exception as e:
                log.warning("Search(topic:%s) 失败：%s", topic, e)

    log.info("双源合并后候选项目数：%d", len(merged))
    return merged


def _pushed_after(focus: dict) -> str:
    return (now() - timedelta(days=focus["pushed_within_days"])).strftime("%Y-%m-%d")


def _classify_ai(candidates: list[dict]) -> dict[str, dict]:
    """判定每个项目是否属于"AI 应用"。优先 LLM，否则关键词兜底。
    返回 {full_name: {"keep": bool, "category": str, "reason": str}}。
    """
    if not candidates:
        return {}

    if llm_client.available():
        try:
            return _classify_ai_llm(candidates)
        except Exception as e:
            log.warning("LLM 分类失败，回退关键词过滤：%s", e)

    return {c["full_name"]: _classify_ai_keyword(c) for c in candidates}


def _classify_ai_llm(candidates: list[dict]) -> dict[str, dict]:
    lines = [
        f'{i}. {c["full_name"]} | {c.get("language")} | topics={c.get("topics")} | {c.get("description","")[:160]}'
        for i, c in enumerate(candidates)
    ]
    prompt = (
        "下面是一批 GitHub 仓库。请判断每个是否属于『AI 应用』"
        "（面向终端用例的 AI 产品/应用/Agent/工具，而非纯数据集、论文清单、"
        "awesome 列表、教程或与 AI 无关的项目）。\n"
        "只输出 JSON：{\"results\":[{\"index\":0,\"keep\":true,\"category\":\"AI 应用\",\"reason\":\"...\"}]}。\n\n"
        + "\n".join(lines)
    )
    data = llm_client.chat_json(
        [{"role": "user", "content": prompt}],
        system="你是严谨的技术分类助手，严格只输出 JSON。",
        retries=1,
    )
    out: dict[str, dict] = {}
    for r in data.get("results", []):
        idx = r.get("index")
        if isinstance(idx, int) and 0 <= idx < len(candidates):
            out[candidates[idx]["full_name"]] = {
                "keep": bool(r.get("keep")),
                "category": r.get("category", "AI 应用"),
                "reason": r.get("reason", ""),
            }
    # 兜底：模型漏判的按关键词补
    for c in candidates:
        out.setdefault(c["full_name"], _classify_ai_keyword(c))
    return out


def _classify_ai_keyword(c: dict) -> dict:
    text = f"{c['full_name']} {c.get('description','')} {' '.join(c.get('topics',[]))}".lower()
    if any(h in text for h in _EXCLUDE_HINTS):
        return {"keep": False, "category": "", "reason": "疑似列表/教程类"}
    keep = bool(_KW_RE.search(text))
    return {"keep": keep, "category": "AI 应用" if keep else "",
            "reason": "关键词命中" if keep else "无 AI 关键词"}


def _rank_score(item: dict, index: dict) -> int:
    """排序用的「热度增量」。Trending 给真实窗口增量；Search 源用历史增量或
    创建以来日均增速兜底，避免纯 Search 项目恒为 0、永远排不上。"""
    if item.get("stars_gained", 0) > 0:
        return item["stars_gained"]
    rec = index.get(item["full_name"])
    if rec and rec.get("last_stars_total"):
        return max(0, item["stars_total"] - rec["last_stars_total"])
    created = item.get("created_at")
    if created:
        try:
            y, m, d = (int(x) for x in created.split("-"))
            age_days = max(1, (now().date() - date(y, m, d)).days)
            return int(item["stars_total"] / age_days)  # 日均增速代理
        except (ValueError, TypeError):
            pass
    return 0


def _decide(item: dict, index: dict) -> tuple[str, str]:
    """基于 index.json 判定 new / revisit / skip。"""
    cfg = get_config()["analyze_revisit"]
    rec = index.get(item["full_name"])
    if rec is None:
        return "new", "首次发现"

    # 复访判定需要 release 信息 → 在 analyze 阶段精确处理；这里用 star 增长粗判
    last_stars = rec.get("last_stars_total", 0)
    if last_stars and item["stars_total"] >= last_stars * (1 + cfg["on_star_jump_pct"] / 100):
        return "revisit", f"star 较上次增长≥{cfg['on_star_jump_pct']}%"
    return "skip_lightweight", "已收录且无显著变化"


def collect() -> list[dict]:
    """返回当天处理清单（已排序、已附 decision）。"""
    gh = _client()
    index = load_index()

    merged = _gather(gh)

    # 手动 blocklist：误判过 / 明确不想要的项目永不收录（config.focus.blocklist）
    blocklist = {b.lower() for b in get_config()["focus"].get("blocklist", [])}
    candidates = [c for c in merged.values() if c["full_name"].lower() not in blocklist]
    if len(candidates) != len(merged):
        log.info("blocklist 过滤掉 %d 个项目", len(merged) - len(candidates))

    verdicts = _classify_ai(candidates)
    _log_classification(candidates, verdicts)
    kept = [c for c in candidates if verdicts.get(c["full_name"], {}).get("keep")]
    log.info("AI 应用过滤后：%d / %d", len(kept), len(candidates))

    for c in kept:
        v = verdicts[c["full_name"]]
        c["category"] = v.get("category", "AI 应用")
        c["classify_reason"] = v.get("reason", "")
        c["rank_score"] = _rank_score(c, index)
        decision, reason = _decide(c, index)
        c["decision"], c["decision_reason"] = decision, reason

    # 排序：热度增量优先（含 Search 源兜底），其次总 star
    kept.sort(key=lambda x: (x["rank_score"], x["stars_total"]), reverse=True)
    return kept


def _log_classification(candidates: list[dict], verdicts: dict[str, dict]) -> None:
    """把当轮全部分类结果（含被丢弃的）落盘，便于回看误判、迭代 prompt。"""
    today = today_str()
    try:
        for c in candidates:
            v = verdicts.get(c["full_name"], {})
            append_jsonl(CLASSIFY_LOG, {
                "date": today,
                "full_name": c["full_name"],
                "source": c.get("source"),
                "keep": v.get("keep"),
                "category": v.get("category", ""),
                "reason": v.get("reason", ""),
                "description": (c.get("description") or "")[:160],
            })
    except Exception as e:
        log.warning("写分类日志失败：%s", e)


if __name__ == "__main__":
    for c in collect():
        print(f'[{c["decision"]:16}] {c["full_name"]:45} '
              f'score={c["rank_score"]:>6} +{c["stars_gained"]}⭐ '
              f'({c["source"]}) {c.get("classify_reason","")}')
