## 安装与启动

**macOS 桌面应用**
1. 从 [Latest release](https://github.com/inkeep/open-knowledge/releases/latest) 下载 DMG
2. 拖拽 OpenKnowledge 到 Applications 并启动

**Linux/Windows/Intel Mac（Web UI 模式）**
- 依赖：Node.js 24+
```bash
npm install -g @inkeep/open-knowledge
cd your-project
ok init          # 初始化项目并自动配置本机的 Claude/Cursor/Codex
ok start --open  # 启动 Web 编辑器并在浏览器打开
```

## 最小可用示例
1. 在项目根目录创建 `notes/getting-started.md`，写入：
```
# Welcome to OpenKnowledge
This note is for my AI agent.
```
2. 在 Claude Code 或 Codex 中直接询问“在笔记中记录下今天的待办”，代理会通过 MCP 写入文件。
3. 在编辑器中即可看到自动更新的内容，并建立双向链接。