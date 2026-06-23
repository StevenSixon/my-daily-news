## 安装
1. 确保使用 macOS 26 (Tahoe) 且 Apple Silicon 芯片的 Mac。
2. 下载 [Palmier Pro DMG](https://github.com/palmier-io/palmier-pro/releases/latest/download/PalmierPro.dmg) 并安装。
3. 首次启动无需登录即可使用基础编辑功能。

## 连接 AI 代理
启动应用后，MCP 服务器自动运行在 `http://127.0.0.1:19789/mcp`。

**Claude Code 示例**：
```bash
claude mcp add --transport http palmier-pro http://127.0.0.1:19789/mcp
```
然后即可在 Claude Code 中让 AI 操作视频项目。

**Cursor 配置**：在应用内 `Help` → `MCP Instructions` 自动安装，或手动在 `~/.cursor/mcp.json` 添加：
```json
{
  "mcpServers": {
    "palmier-pro": {
      "type": "http",
      "url": "http://127.0.0.1:19789/mcp"
    }
  }
}
```

## 最小可用示例
1. 打开 Palmier Pro，创建一个新项目。
2. 在 Claude Code 终端中执行自然语言指令，例如 “在当前项目中导入 video.mp4 并放到第一轨道”。
3. AI 将通过 MCP 操控时间线完成导入和放置。

## 依赖前提
- 硬件：Apple Silicon Mac。
- 系统：macOS 26 Tahoe。
- 生成式 AI 功能：需账户和订阅。