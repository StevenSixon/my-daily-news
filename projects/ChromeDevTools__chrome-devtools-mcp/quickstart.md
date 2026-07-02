## 依赖
- Node.js LTS 版本
- Chrome 当前稳定版 或 Chrome for Testing
- npm

## 安装与最小可用示例
在 MCP 客户端配置文件（如 Claude Desktop 的 `mcpServers` 配置）中添加：
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```
重启客户端后，即可在对话中让 AI 使用 Chrome DevTools 工具。

若只想做基本浏览器任务，可启用精简模式：
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest", "--slim", "--headless"]
    }
  }
}
```

也可用 Claude Code CLI 快速添加：
```bash
claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest
```

启动后 AI 代理即可执行 `take_screenshot`、`navigate_page`、`performance_start_trace` 等操作。