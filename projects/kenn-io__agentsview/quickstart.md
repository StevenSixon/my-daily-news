## 安装
- macOS/Linux: `curl -fsSL https://agentsview.io/install.sh | bash`
- Windows: `powershell -ExecutionPolicy ByPass -c "irm https://agentsview.io/install.ps1 | iex"`
- 桌面应用: `brew install --cask agentsview` 或从GitHub Releases下载
- Docker: `docker pull ghcr.io/kenn-io/agentsview:latest`

## 最小可用示例
1. 启动服务并打开Web UI：
   ```bash
   agentsview serve
   ```
   浏览器访问 `http://127.0.0.1:8080`。
2. 查看每日费用摘要：
   ```bash
   agentsview usage daily
   ```
3. 后台运行并停止：
   ```bash
   agentsview serve --background
   agentsview serve stop
   ```

## 依赖前提
- 无外部依赖，只需下载agentsview二进制或运行Docker。
- 确保机器上安装了至少一个支持的AI代理会话目录，以便有数据可展示。
- 如需远程访问，正确设置`--public-url`。