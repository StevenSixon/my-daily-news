## 安装与使用

### 前提
- 安装并运行 Hermes Agent，开启 API 服务器（默认端口 8642）
- Node.js 20+
- Chrome 114+ 或基于 Chromium 的浏览器（Edge、Brave 等）

### 构建扩展
```bash
git clone https://github.com/abundantbeing/hermes-browser-extension.git
cd hermes-browser-extension
npm install
npm run build
```
生成的 `dist/` 目录即为可加载的扩展。

### 加载到浏览器
1. 打开 `chrome://extensions`，启用“开发者模式”
2. 点击“加载已解压的扩展程序”，选择 `dist/` 文件夹
3. 点击工具栏的 Hermes 图标打开侧边栏

### 连接 Hermes
- 本地连接：确保 Hermes 网关运行，扩展中点击“连接到 Hermes”，选择“本地网关”，填入 `http://127.0.0.1:8642` 及 API 密钥，测试连接后保存
- 远程连接：选择“远程网关”，输入可访问的 URL（如 `https://hermes.example.com`）及 API 密钥
- 无 API 密钥的仪表板模式：选择远程，输入仪表板 HTTPS URL，保持密钥为空，通过已登录的仪表板标签页获取一次性 WebSocket 票证连接

### 快速测试
打开任意示例页面，在侧边栏输入 “Summarize this page in one sentence.” 即可验证。