## 安装

**macOS**：从 [Releases](https://github.com/inkeep/open-knowledge/releases/latest) 下载 DMG，拖入应用程序即可。

**其他平台**：需 Node.js 24+，执行：
```bash
npm install -g @inkeep/open-knowledge
cd your-project
ok init          # 初始化项目，自动配置代理
ok start --open  # 启动 Web 编辑器并打开浏览器
```

## 最小使用

- 创建一个新笔记本：`mkdir my-notes && cd my-notes && ok init && ok start --open`
- 打开已有 Markdown 文件夹（如 Obsidian 仓库）：在应用中选择文件夹即可，编辑器自动识别现有文件。
- 在编辑器中按下“Ask AI”或使用快捷键唤出 Agent 对话，选择已接入的 Claude/Codex 等，让 AI 协助撰写或修改。

## 依赖前提

- Node.js >= 24（Web 部署及 CLI）
- macOS 桌面应用为独立包，无需额外环境
- 如需 AI 代理功能，须确保本机已安装对应的 Agent 工具（如 Claude Code、Cursor、Codex CLI 等）