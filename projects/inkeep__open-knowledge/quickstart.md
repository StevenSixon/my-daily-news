## 安装
**macOS**：从 [最新 Release](https://github.com/inkeep/open-knowledge/releases/latest) 下载 DMG，拖入应用文件夹。

**其他平台**（需 Node.js ≥ 24）：
```bash
npm install -g @inkeep/open-knowledge
cd your-project
ok init          # 脚手架项目并自动配置 AI Agent
ok start --open  # 启动本地 Web 编辑器并打开浏览器
```

## 最小可用示例
1. 创建或进入一个包含 Markdown 文件的文件夹。
2. 执行 `ok init`，将自动检测 Claude Code / Codex / Cursor 等并生成 MCP 配置。
3. 运行 `ok start --open`，在浏览器中编辑文档，用 ⌘L 呼出 AI 聊天。

## 依赖前提
- Node.js 24+
- 如果需要 AI 功能，至少安装一种 CLI Agent（Claude Code / Codex / Cursor / OpenCode）