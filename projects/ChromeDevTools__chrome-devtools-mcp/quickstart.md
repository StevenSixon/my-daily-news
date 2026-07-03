## 安装前准备
- 安装 Node.js LTS 版本（https://nodejs.org/）
- 安装 Chrome 最新稳定版或 Chrome for Testing（https://developer.chrome.com/blog/chrome-for-testing/）
- 确认 npm 可用

## 最小可用配置（以Claude Code为例）
```bash
# 在终端中添加MCP服务器，scope user表示全局生效
claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest
```
重启Claude Code后，即可在对话中让代理操作浏览器：
> “打开 https://example.com，检查控制台错误，并分析性能”

## 通用的MCP客户端配置
如果你的AI客户端需要手动编辑配置文件，添加：
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

## 可选模式
- **Slim模式**（仅基础工具，更快启动）：加上 `--slim` 参数。
- **无头模式**：加上 `--headless`。
- **禁用性能CrUX数据**：加上 `--no-performance-crux`。

## 开箱即用示例
- 截图：代理调用 `take_screenshot` 工具。
- 性能分析：代理调用 `performance_start_trace`，操作后调用 `performance_stop_trace` 获取指标。
- 网络检查：使用 `list_network_requests` 查看所有请求，`get_network_request` 获取详情。