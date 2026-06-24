### 前提条件
- Node.js 环境（可执行 npx）
- 目标 AI 编码代理已安装或可访问（如 Grok、Claude Code 或 Codex）

### 5 分钟快速开始
```bash
# 1. 用 daily-triage 模式脚手架项目（以 Grok 为例）
npx @cobusgreyling/loop-init . --pattern daily-triage --tool grok

# 2. 估算 token 花费（L1 报告级别）
npx @cobusgreyling/loop-cost --pattern daily-triage --level L1

# 3. 审计当前目录的准备度
npx @cobusgreyling/loop-audit . --suggest

# 4. 在 AI 代理界面（如 Grok）中启动仅报告循环
/loop 1d Run loop-triage. Update STATE.md. No auto-fix in week one.
```
### 开发者（从源码使用）
```bash
cd tools/loop-init && npm ci && npm test && node dist/cli.js /path/to/project --pattern daily-triage --tool grok
cd tools/loop-audit && npm ci && npm test && node dist/cli.js /path/to/project --suggest
cd tools/loop-cost && npm ci && npm test && node dist/cli.js --pattern ci-sweeper --cadence 15m
```