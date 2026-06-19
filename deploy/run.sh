#!/usr/bin/env bash
# launchd 调用入口：用 venv 绝对路径运行指定阶段（避免依赖交互 shell）
# 用法：run.sh pipeline [--top-n 5]   |   run.sh push
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

PYTHON="$PROJECT_DIR/.venv/bin/python"
STAGE="${1:-pipeline}"
shift || true  # 后面的参数透传给 python -m src.<stage>

case "$STAGE" in
  pipeline)
    "$PYTHON" -m src.pipeline "$@"
    # 流水线跑完后刷新看板数据并重建单文件 artifact（失败不影响主流程）
    bash "$PROJECT_DIR/dashboard/refresh.sh" || true
    ;;
  push)     exec "$PYTHON" -m src.push      "$@" ;;
  *) echo "未知阶段：$STAGE（应为 pipeline 或 push）" >&2; exit 1 ;;
esac
