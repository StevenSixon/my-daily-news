#!/usr/bin/env bash
# Dead-man's-switch 健康检查：确认"当日日报"已生成，否则推飞书告警。
#
# 为什么需要它：pipeline.py 自身只在"跑起来但失败"时告警；如果 06:30 任务
# 根本没触发（最常见：Mac 在睡眠，launchd StartCalendarInterval 不唤醒），
# 那条告警永远发不出。本检查独立在稍后时段运行，专门兜住"静默没跑"。
#
# 用法：
#   deploy/healthcheck.sh                # 检查今天
#   deploy/healthcheck.sh 2026-06-19     # 检查指定日期（测试用）
#   HEALTHCHECK_DRY=1 deploy/healthcheck.sh   # 只打印不真正发飞书
set -uo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"
PYTHON="$PROJECT_DIR/.venv/bin/python"
DAY="${1:-$(date +%F)}"
FILE="daily/$DAY.json"

if [ -f "$FILE" ]; then
  CNT="$("$PYTHON" -c "import json;print(json.load(open('$FILE')).get('count','?'))" 2>/dev/null || echo '?')"
  echo "[healthcheck] OK：${DAY} 日报已生成（${CNT} 个项目）"
  exit 0
fi

TITLE="⚠️ AI 日报未生成（${DAY}）"
LINES="${DAY} 未检测到当日日报 ${FILE}|可能：Mac 在 06:30 睡眠未触发，或流水线异常|排查：launchctl list ｜ grep daily ；tail logs/launchd.pipeline.err.log"
echo "[healthcheck] 缺失：${FILE}" >&2

case "${HEALTHCHECK_DRY:-0}" in
  1 | true | yes | on)
    echo "[healthcheck] DRY：将发送告警 → ${TITLE}"
    echo "[healthcheck] DRY：内容 → ${LINES}"
    exit 1
    ;;
esac

if [ ! -x "$PYTHON" ]; then
  echo "[healthcheck] 找不到 venv python，无法发送告警：$PYTHON" >&2
  exit 1
fi

"$PYTHON" - "$TITLE" "$LINES" <<'PY' 2>/dev/null || echo "[healthcheck] 飞书告警发送失败" >&2
import sys
from src import feishu_client
feishu_client.send_alert(sys.argv[1], sys.argv[2].split("|"), "red")
PY
exit 1
