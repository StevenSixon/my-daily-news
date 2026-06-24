## 安装

1. 确保使用 **Apple Silicon 芯片** 并升级至 **macOS 26 (Tahoe)**。
2. 从 [GitHub Releases](https://github.com/palmier-io/palmier-pro/releases/latest/download/PalmierPro.dmg) 下载 DMG，安装到 Applications。
3. 首次打开可能需在“系统设置 > 隐私与安全性”中允许运行。

## 启用 MCP 服务

启动 Palmier Pro 后，MCP 服务器会自动监听 `http://127.0.0.1:19789/mcp`。无需额外配置。

## 连接 AI 助手

**Claude Code**
```bash
claude mcp add --transport http palmier-pro http://127.0.0.1:19789/mcp
```

**Cursor**

打开 App 内 `Help → MCP Instructions → Install in Cursor` 或手动编辑 `~/.cursor/mcp.json`：
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

**Codex**
```bash
codex mcp add palmier-pro --url http://127.0.0.1:19789/mcp
```

## 最小可用示例

1. 打开 Palmier Pro，新建或打开一个项目。
2. 启动你的 AI 客户端（如 Claude Code），询问：“请在时间线上添加一个剪辑，并应用淡入效果。”
3. AI 助手通过 MCP 操作时间线，你在编辑器中实时看到变化。

## 依赖前提

- 硬件：Apple Silicon Mac（M1 或更新）
- 系统：macOS 26 及以上
- 编辑器本身无需账户，生成式 AI 功能需注册并登录 Palmier 账户。