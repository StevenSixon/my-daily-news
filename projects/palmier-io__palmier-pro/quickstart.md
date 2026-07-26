## 安装
1. 前往 [Releases](https://github.com/palmier-io/palmier-pro/releases/latest) 下载 `PalmierPro.dmg`。
2. 打开 DMG，将应用拖入 `Applications` 文件夹。
3. 启动应用（需 macOS 26 Apple Silicon）。

## 连接 AI 代理（最小示例）
应用启动后，MCP 服务器自动运行在 `http://127.0.0.1:19789/mcp`。

### Claude Code
```bash
claude mcp add --transport http palmier-pro http://127.0.0.1:19789/mcp
```
### Codex
```bash
codex mcp add palmier-pro --url http://127.0.0.1:19789/mcp
```
### Cursor
在应用内 `Help` -> `MCP Instructions` -> `Install in Cursor`，或手动编辑 `~/.cursor/mcp.json` 添加：
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
### Claude Desktop
通过应用内的 `Help` -> `MCP Instructions` -> `Install in Claude Desktop` 一键安装（依赖内置 mcpb）。

## 使用编辑器
无需登录，打开即可免费使用所有剪辑功能。如需使用生成式 AI 生成视频/图像，则需登录并订阅。