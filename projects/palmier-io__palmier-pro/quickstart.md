## 安装
- 下载 DMG：从 [Releases](https://github.com/palmier-io/palmier-pro/releases/latest) 获取 `PalmierPro.dmg`，拖入 Applications。
- 系统要求：macOS 26 (Tahoe) 且仅支持 Apple Silicon（M 系列芯片）。
- 打开应用：首次可能需允许来自不明开发者的安全提示。

## 最小可用示例（用 Claude Code 剪辑）
1. 启动 Palmier Pro 并保持运行。
2. 在终端添加 MCP 连接：
   ```bash
   claude mcp add --transport http palmier-pro http://127.0.0.1:19789/mcp
   ```
3. 在 Claude Code 会话中用自然语言操作，例如：
   “打开项目 123，将第三轨道上 00:02:10 到 00:02:30 的片段静音并删除。”
   Claude 会通过 MCP 工具调用时间线 API。
4. 也可在 Cursor/Codex 中配置对应的 mcp.json，详见 README。

## 依赖前提
- 仅需 macOS 26 与 Apple Silicon，无需额外语言运行时或包管理器。