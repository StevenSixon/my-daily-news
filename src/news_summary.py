"""资讯加工：打分排序 → 跨源 LLM 聚类去重 → 来源配额 → 截断到 max_items
→ LLM 中文一句话摘要 + 分类。

复用 llm_client（与项目分析同一套多模型可插拔配置）。LLM 不可用或
news.llm_summarize=false 时优雅降级为仅标题聚合（零 LLM 成本、无去重）。
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
    """批量生成中文一句话摘要 + 分类 + 事件标识（跨源去重用）。
    失败则保留空字段（由渲染/去重层兜底）。"""
    lines = [
        f'{i}. [{it["source"]}] {it["title"]}'
        + (f' — {it["summary_raw"][:160]}' if it.get("summary_raw") else "")
        for i, it in enumerate(items)
    ]
    prompt = (
        "下面是一批 AI 领域的资讯标题（含来源，部分附原文摘要）。"
        "请为每条生成：\n"
        "1) summary_zh：一句话中文摘要（≤40 字，客观、点出关键信息，不要营销腔）；\n"
        f"2) category：从 {_CATEGORIES} 中选最贴切的一个；\n"
        "3) event_key：该资讯所述事件的简短英文标识（小写、下划线连接，如 "
        "openai_gpt55_release）。报道【同一事件】的多条必须给【相同】 event_key，"
        "用于跨源去重；不同事件给不同 key。\n"
        '只输出 JSON：{"results":[{"index":0,"summary_zh":"...","category":"模型发布",'
        '"event_key":"..."}]}。\n\n'
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
            items[idx]["_event_key"] = (r.get("event_key") or "").strip().lower()
    return items


def _dedupe_by_event(items: list[dict]) -> list[dict]:
    """按 LLM 给出的 event_key 跨源去重，保留先出现者（即得分更高的代表）。
    无 event_key 的条目一律保留。"""
    seen: set[str] = set()
    out: list[dict] = []
    for it in items:
        key = it.get("_event_key")
        if key:
            if key in seen:
                continue
            seen.add(key)
        out.append(it)
    return out


def _apply_quota(items: list[dict]) -> list[dict]:
    """按得分序丢弃超额条目，保留原序、不限总数。两道闸：
    - news.per_source_max：每个具体来源（如 Claude）最多 N 条，防单家刷屏；
    - news.type_quota：每类来源（official/paper/community…）的上限，防某类刷屏。
    未配置者不限量。"""
    cfg = _cfg()
    type_quota = cfg.get("type_quota", {}) or {}
    per_source = cfg.get("per_source_max")  # None = 每来源不限
    type_counts: dict[str, int] = {}
    src_counts: dict[str, int] = {}
    out: list[dict] = []
    for it in items:
        st = it.get("source_type", "")
        src = it.get("source", "")
        tcap = type_quota.get(st)
        if tcap is not None and type_counts.get(st, 0) >= tcap:
            continue
        if per_source is not None and src_counts.get(src, 0) >= per_source:
            continue
        out.append(it)
        type_counts[st] = type_counts.get(st, 0) + 1
        src_counts[src] = src_counts.get(src, 0) + 1
    return out


def summarize(candidates: list[dict]) -> list[dict]:
    """打分排序 → 来源配额 → 跨源 LLM 聚类去重 → 截断 → LLM 摘要。

    先按配额裁出多样化的候选（论文不刷屏），再送 LLM 加工/去重，
    最后截断到 max_items。配额前置可避免 LLM 池被单一来源占满。"""
    cfg = _cfg()
    if not candidates:
        return []

    max_items = int(cfg.get("max_items", 12))
    ranked = sorted(candidates, key=_score, reverse=True)
    # 先施加来源配额，得到多样化的有序候选；再取 LLM 池（含去重余量，控成本）
    pool = _apply_quota(ranked)[: max(max_items * 2, max_items)]

    use_llm = cfg.get("llm_summarize", True) and llm_client.available()
    if use_llm:
        try:
            pool = _llm_enrich(pool)
            before = len(pool)
            pool = _dedupe_by_event(pool)
            if before != len(pool):
                log.info("资讯：跨源去重合并 %d 条", before - len(pool))
        except Exception as e:
            log.warning("资讯 LLM 摘要/去重失败，降级为仅标题：%s", e)

    selected = pool[:max_items]

    out = []
    for it in selected:
        out.append({
            "title": it["title"],
            "url": it["url"],
            "source": it["source"],
            "source_type": it["source_type"],
            "published": it.get("published", ""),
            "summary_zh": it.get("summary_zh", ""),
            "category": it.get("category", ""),
        })
    log.info("资讯：采纳 %d 条（LLM 摘要/去重=%s）", len(out), use_llm)
    return out
