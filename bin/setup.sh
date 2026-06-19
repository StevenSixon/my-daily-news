#!/usr/bin/env bash
# ===== AI 项目日报助理 一键安装脚本 =====
# 用法：bash bin/setup.sh
set -euo pipefail

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'
say() { printf "${GREEN}✓${NC} %s\n" "$1"; }
warn() { printf "${YELLOW}⚠${NC} %s\n" "$1"; }
die() { printf "${RED}✗${NC} %s\n" "$1"; exit 1; }

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

echo "======== AI 项目日报助理 · 安装 ========"
echo ""

# 1. 检查 Python
PYTHON=""
for py in python3 python3.12 python3.11 python3.10; do
  if command -v "$py" &>/dev/null && "$py" -c 'import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)' 2>/dev/null; then
    PYTHON="$py"; break
  fi
done
[ -n "$PYTHON" ] || die "未找到 Python 3.10+，请先安装。"
say "Python: $($PYTHON --version)"

# 2. 创建虚拟环境
if [ -d ".venv" ]; then
  warn "虚拟环境已存在，跳过创建。"
else
  "$PYTHON" -m venv .venv
  say "虚拟环境已创建。"
fi

# 3. 安装依赖
.venv/bin/pip install -q -r requirements.txt 2>&1 | tail -1
say "依赖已安装。"

# 4. 检查 .env
if [ ! -f ".env" ]; then
  warn ".env 不存在，从 .env.example 复制…"
  cp .env.example .env
  warn "请编辑 .env 填入密钥后重新运行："
  echo "     vim .env"
  echo "     bash bin/setup.sh"
  exit 1
fi

# 检查必要密钥
ENV_OK=true
check_env() {
  local val; val=$(grep -E "^${1}=" .env 2>/dev/null | cut -d= -f2- || true)
  if [ -z "$val" ] || [ "$val" = '""' ] || [ "$val" = "''" ]; then
    warn "缺少 $1（.env 中为空）"
    ENV_OK=false
  fi
}
check_env "GITHUB_TOKEN"
check_env "FEISHU_APP_ID"
check_env "FEISHU_APP_SECRET"
check_env "FEISHU_RECEIVE_ID"
check_env "FEISHU_RECEIVE_ID_TYPE"
# LLM key 至少需要一个
LLM_KEYS=$(grep -cE '^(ANTHROPIC|OPENAI|DEEPSEEK|GEMINI|OPENAI_COMPATIBLE)_API_KEY=.{10,}' .env 2>/dev/null || true)
if [ "$LLM_KEYS" -eq 0 ]; then
  warn "未配置任何 LLM API KEY，系统将跳过深度学习（仅采集+元数据）。"
fi
if [ "$ENV_OK" = false ]; then
  echo ""; warn "请补充上述密钥后重新运行 bash bin/setup.sh"; exit 1
fi
say ".env 配置检查通过。"

# 5. 验证流水线（仅采集，不调 LLM）
echo ""
echo ">>> 验证流水线（采集双源，不调用 LLM）…"
if ANTHROPIC_API_KEY="" DEEPSEEK_API_KEY="" OPENAI_API_KEY="" GEMINI_API_KEY="" \
   timeout 120 .venv/bin/python -m src.collect > /dev/null 2>&1; then
  say "采集验证通过。"
else
  warn "采集验证未完全通过（可能是网络/GitHub API 问题），但不影响后续安装。"
fi

# 6. 安装 launchd 定时任务
echo ""
PLIST_DIR="$HOME/Library/LaunchAgents"
mkdir -p "$PLIST_DIR"

install_plist() {
  local name="$1" time="$2"
  local plist="$PLIST_DIR/com.daily-news.${name}.plist"
  local src="$PROJECT_DIR/deploy/com.daily-news.${name}.plist"

  # 如果模板存在且还未安装
  if [ -f "$plist" ]; then
    warn "launchd 任务 daily-news.${name} 已存在，跳过。如需重装："
    echo "     launchctl unload $plist && rm $plist && bash bin/setup.sh"
    return
  fi

  cat > "$plist" <<PLIST_EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.daily-news.${name}</string>
  <key>ProgramArguments</key>
  <array>
    <string>$PROJECT_DIR/.venv/bin/python</string>
    <string>-m</string>
    <string>src.${name/pipeline/pipeline}</string>
PLIST_EOF

  if [ "$name" = "pipeline" ]; then
    cat >> "$plist" <<EOF
    <string>--top-n</string>
    <string>5</string>
EOF
  fi

  cat >> "$plist" <<PLIST_EOF
  </array>
  <key>WorkingDirectory</key>
  <string>$PROJECT_DIR</string>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Hour</key><integer>${time%:*}</integer>
    <key>Minute</key><integer>${time#*:}</integer>
  </dict>
  <key>StandardOutPath</key>
  <string>$PROJECT_DIR/logs/launchd.${name}.out.log</string>
  <key>StandardErrorPath</key>
  <string>$PROJECT_DIR/logs/launchd.${name}.err.log</string>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key>
    <string>/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/homebrew/bin</string>
  </dict>
  <key>RunAtLoad</key>
  <false/>
</dict>
</plist>
PLIST_EOF

  launchctl load "$plist" 2>/dev/null
  say "launchd daily-news.${name} 已安装（每天 ${time} 触发）。"
}

install_plist "pipeline" "6:30"
install_plist "push"     "8:00"

echo ""
echo "======== 安装完成 ========"
say "流水线：每天 06:30 自动运行"
say "推送：  每天 08:00 自动推送飞书"
echo ""
echo "手动命令："
echo "  python -m src.pipeline        # 跑一次完整流水线"
echo "  python -m src.push            # 推送到飞书"
echo "  launchctl list | grep daily   # 查看定时任务状态"
echo ""
echo "⚠️  Mac 睡眠时会延迟触发，建议保持唤醒或插电。"
