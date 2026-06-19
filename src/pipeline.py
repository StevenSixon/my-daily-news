"""编排：collect → analyze（写项目库）→ build_summary（写日报）。

不含推送（推送由 push.py 在 08:00 单独执行，错峰保证准时）。
"""
from __future__ import annotations

import argparse

from . import analyze, build_summary, collect, llm_client
from .config_loader import get_config
from .store import load_index, save_index
from .utils import get_logger

log = get_logger()


def run(top_n: int | None = None) -> dict:
    if not llm_client.available():
        log.warning("当前无可用 LLM key：将跳过深度学习，仅采集+更新元数据。")

    candidates = collect.collect()

    top_n = top_n or get_config()["collect"]["top_n"]
    # 取需要处理的：new / revisit 优先，跳过的轻量项目也保留少量用于"持续上榜"展示
    to_learn = [c for c in candidates if c["decision"] in ("new", "revisit")][:top_n]
    log.info("本轮深度处理 %d 个项目（top_n=%d）", len(to_learn), top_n)

    index = load_index()
    items = []
    for c in to_learn:
        try:
            items.append(analyze.learn(c, index))
        except Exception as e:
            log.warning("处理 %s 失败：%s", c["full_name"], e)
    save_index(index)

    payload = build_summary.build(items)
    log.info("Pipeline 完成。")
    return payload


def main():
    ap = argparse.ArgumentParser(description="AI 项目日报 pipeline（采集+学习+日报）")
    ap.add_argument("--top-n", type=int, default=None, help="本轮最多深度学习的项目数")
    args = ap.parse_args()
    run(top_n=args.top_n)


if __name__ == "__main__":
    main()
