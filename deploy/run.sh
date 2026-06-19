#!/usr/bin/env bash
# launchd 调用入口：激活虚拟环境并运行指定阶段
# 用法：run.sh pipeline | push
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

# 若存在 venv 则激活（按需修改）
if [ -d ".venv" ]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

STAGE="${1:-pipeline}"
case "$STAGE" in
  pipeline) exec python -m src.pipeline ;;
  push)     exec python -m src.push ;;
  *) echo "未知阶段：$STAGE（应为 pipeline 或 push）" >&2; exit 1 ;;
esac
