## 安装与构建
```bash
git clone https://github.com/abundantbeing/hermes-browser-extension.git
cd hermes-browser-extension
npm install
npm run build
```
生成的 `dist/` 即扩展目录。

## 加载到 Chrome
1. 打开 `chrome://extensions`，启用“开发者模式”。
2. 点击“加载已解压的扩展程序”，选择 `dist/` 文件夹。
3. 点击工具栏扩展图标打开侧面板。

## 连接 Hermes
- **本地模式**：确保 Hermes Gateway 已在 `127.0.0.1:8642` 运行，并配置 `API_SERVER_KEY`。
- 扩展侧面板中点击“Manual setup”，选择“Local gateway”，输入 `http://127.0.0.1:8642` 和你的浏览器 token/API key，测试连接后保存。
- **远程模式**：类似但填写可访问的远程 URL。

## 最小示例
打开任意 `https://` 页面（如一篇博客），在侧面板中输入：“Summarize this page in one sentence.” 即可获得基于上下文的摘要。可试用 `/summarize` 快速命令。

**依赖**：Node.js 20+，Chrome 114+，已安装并运行 Hermes Agent。