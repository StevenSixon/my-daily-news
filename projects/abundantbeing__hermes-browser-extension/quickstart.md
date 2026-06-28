### 1. 准备工作
- 确保已安装并运行 Hermes Agent，且 API 服务器已启用。
- 在 Hermes 的 `~/.hermes/.env` 中配置如下（示例）：
  ```bash
  API_SERVER_ENABLED=true
  API_SERVER_HOST=127.0.0.1
  API_SERVER_PORT=8642
  API_SERVER_KEY=<your-key>
  API_SERVER_CORS_ORIGINS=chrome-extension://<extension-id>
  ```
  启动网关：`hermes gateway run`
- 本机需有 Node.js 20+ 和 Chrome/Edge 114+ 浏览器。

### 2. 构建扩展
```bash
git clone https://github.com/abundantbeing/hermes-browser-extension.git
cd hermes-browser-extension
npm install
npm run build
```
生成的扩展目录为 `dist/`。

### 3. 加载扩展
进入 `chrome://extensions` 或 `edge://extensions`，开启开发者模式，点击“加载已解压的扩展”，选择 `dist/` 文件夹。

### 4. 连接 Hermes 并测试
点击扩展图标打开侧面板，选择“Connect to Hermes” -> “Manual setup”（如果自动审批不可用时），选择 Local gateway，填入 `http://127.0.0.1:8642` 及你的 API 密钥，点击“Test connection”确认连通性后保存。

打开一个正常的 HTTPS 网页（如一篇博客），在侧面板输入：“Summarize this page in one sentence.” 即可看到 Agent 的回复。