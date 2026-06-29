**macOS**：
从 [Latest release](https://github.com/inkeep/open-knowledge/releases/latest) 下载 DMG，拖入 Applications 后直接打开。

**Linux/Windows/Intel Mac（Web 模式）**：
```bash
npm install -g @inkeep/open-knowledge   # 需 Node.js ≥24
cd your-project
ok init          # 初始化项目，并自动配置 Claude/Codex 等
ok start --open  # 启动本地 Web 编辑器
```
之后在浏览器中即可编辑 Markdown 文件，所有数据均在你的项目文件夹内。

**依赖前提**：Node.js 24+，git（可选，用于同步功能）。如需要桌面 AI 集成，需预先安装 Claude Desktop 或 Codex 等。