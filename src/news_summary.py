"""资讯加工：打分排序 → 截断到 max_items → LLM 中文一句话摘要 + 分类。

复用 llm_client（与项目分析同一套多模型可插拔配置）。LLM 不可用或
news.llm_summarize=false 时优雅降级为仅标题聚合（零 LLM 成本）。
"""
from __future__ import annotations

from . import llm_client
from .config_loader import get_config
from .utils import get_logger, now

log = get_logger()

# 来源类型基础权重（一手 > 论文/HF > 社区）
_TYPE_WEIGHT = {"official": 100, "paper": 70, "hf": 70, "community": 45}

_CATEGORIES = ["模型发布", "研究", "产品", "工程", "融资/商业", "观点", "其他"]


def _cfg() -> dict:
    return get_config().get("news", {}) or {}


def _score(it: dict) -> float:
    base = _TYPE_WEIGHT.get(it.get("source_type"), 40)
    # 时效加成：越新越高（窗口内按天衰减）
    ts = it.get("_ts") or 0
    recency = 0.0
    if ts:
        age_days = max(0.0, (now().timestamp() - ts) / 86400)
        recency = max(0.0, 25 - age_days * 8)  # 当天+25，约 3 天后归零
    # HN 点赞作为社区热度信号（封顶，避免压过一手源）
    hn = min(it.get("points", 0) / 8.0, 30) if it.get("source_type") == "community" else 0
    return base + recency + hn


def _llm_enrich(items: list[dict]) -> list[dict]:
    """批量生成中文一句话摘要 + 分类。失败则保留空字段（由渲染层兜底）。"""
    lines = [
        f'{i}. [{it["source"]}] {it["title"]}'
        + (f' — {it["summary_raw"][:160]}' if it.get("summary_raw") else "")
        for i, it in enumerate(items)
    ]
    prompt = (
        "下面是一批 AI 领域的资讯标题（含来源，部分附原文摘要）。"
        "请为每条生成：\n"
        "1) summary_zh：一句话中文摘要（≤40 字，客观、点出关键信息，不要营销腔）；\n"
        f"2) category：从 {_CATEGORIES} 中选最贴切的一个。\n"
        '只输出 JSON：{"results":[{"index":0,"summary_zh":"...","category":"模型发布"}]}。\n\n'
        + "\n".join(lines)
    )
    data = llm_client.chat_json(
        [{"role": "user", "content": prompt}],
        system="你是严谨的 AI 科技编辑，严格只输出 JSON。",
        retries=1,
    )
    for r in data.get("results", []):
        idx = r.get("index")
        if isinstance(idx, int) and 0 <= idx < len(items):
            cat = r.get("category", "")
            items[idx]["summary_zh"] = (r.get("summary_zh") or "").strip()
            items[idx]["category"] = cat if cat in _CATEGORIES else "其他"
    return items


def summarize(candidates: list[dict]) -> list[dict]:
    """打分排序 → 截断 → （可选）LLM 摘要。返回最终进日报的资讯列表。"""
    cfg = _cfg()
    if not candidates:
        return []

    max_items = int(cfg.get("max_items", 12))
    ranked = sorted(candidates, key=_score, reverse=True)[:max_items]

    use_llm = cfg.get("llm_summarize", True) and llm_client.available()
    if use_llm:
        try:
            ranked = _llm_enrich(ranked)
        except Exception as e:
            log.warning("资讯 LLM 摘要失败，降级为仅标题：%s", e)

    # 兜底字段 + 清理内部排序键
    out = []
    for it in ranked:
        out.append({
            "title": it["title"],
            "url": it["url"],
            "source": it["source"],
            "source_type": it["source_type"],
            "published": it.get("published", ""),
            "summary_zh": it.get("summary_zh", ""),
            "category": it.get("category", ""),
        })
    log.info("资讯：采纳 %d 条（LLM 摘要=%s）", len(out), use_llm)
    return out
