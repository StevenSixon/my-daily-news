## 安装
- 系统要求：macOS 26 (Tahoe) + Apple Silicon 芯片
- 下载最新 DMG：[v0.3.4 Release](https://github.com/palmier-io/palmier-pro/releases/latest/download/PalmierPro.dmg)
- 安装并打开，MCP 服务器会自动在 `http://127.0.0.1:19789/mcp` 上启动

## 连接 Claude Code（示例）
```bash
claude mcp add --transport http palmier-pro http://127.0.0.1:19789/mcp
```
然后你可以让 Claude 执行操作，例如：
> 获取当前时间线的转录，并删除所有包含“em”的填充词区间。

## 其他 Agent 接入
- **Codex**: `codex mcp add palmier-pro --url http://127.0.0.1:19789/mcp`
- **Cursor**: 在 app 内 `Help` -> `MCP Instructions` -> `Install in Cursor` 或手动编辑 `~/.cursor/mcp.json`
- **Claude Desktop**: 使用 `Help` -> `MCP Instructions` -> `Install in Claude Desktop` 一键安装

## 最小可用验证
1. 打开 Palmier Pro，导入一段带语音的视频。
2. 在上述 agent 中执行 MCP 工具 `get_transcript` 查看返回的转录文本。
3. 使用 `ripple_delete_ranges` 删除一个区间，观察时间线变化。