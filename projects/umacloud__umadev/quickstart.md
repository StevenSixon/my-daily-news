## 安装
```bash
npm install -g umadev
```
确保已安装并登录至少一个 AI 编码 CLI（任选）：
- Claude Code: `npm i -g @anthropic-ai/claude-code && claude auth login`
- Codex: `npm i -g @openai/codex && codex login`
- OpenCode: 见 opencode.ai 的安装和登录指南

## 最小可用示例
1. 启动交互式 UI：
```bash
umadev
```
2. 输入需求，例如：
```text
build me a todo app with a Postgres backend
```
umaDev 将自动路由任务，展示意图卡片，执行完整的团队流程。

非交互式运行：
```bash
umadev run "add CSV export to the reports page" --backend claude-code
```

首次运行会自动下载本地嵌入模型（约224MB），如网络受限可接受仅 BM25 回退。