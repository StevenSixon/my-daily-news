## 安装
```bash
npm install -g umadev
```
(需要 Node.js 环境，预编译 Rust 二进制通过 npm 分发)

## 依赖前提
- 至少一个已安装并登录的 AI 编程 CLI：
  - Claude Code: `npm i -g @anthropic-ai/claude-code && claude auth login`
  - 或 Codex: `npm i -g @openai/codex && codex login`
  - 或 OpenCode: 从 opencode.ai 安装并 `opencode auth login`

## 最小可用示例
```bash
umadev                          # 启动聊天 UI，首次运行选择基础 CLI
```
然后输入需求：
```
> build me a todo app with a Postgres backend
```
或非交互式运行：
```bash
umadev run "add CSV export to the reports page" --backend claude-code
```
工作会在隔离分支 `umadev/<slug>` 上进行，构建完成后可在 `output/` 目录查看交付包。