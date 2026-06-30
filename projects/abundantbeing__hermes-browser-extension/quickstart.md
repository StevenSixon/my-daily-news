## 安装要求
- 安装并运行 Hermes Agent（需配置 API 服务器，开启 HTTPS/HTTP）
- Node.js 20+
- Chrome/Edge 114+ 浏览器

## 构建与加载
```bash
git clone https://github.com/abundantbeing/hermes-browser-extension.git
cd hermes-browser-extension
npm install
npm run build
```
在浏览器扩展管理页面开启开发者模式，加载 `dist/` 文件夹。

## 连接 Hermes
1. 在 Hermes 网关配置中启用 API 服务器，设置 KEY 和 CORS 允许 `chrome-extension://<扩展ID>`。
2. 启动网关。
3. 在扩展侧边栏选择“手动设置” -> “本地网关”，填入 `http://127.0.0.1:8642` 和 API KEY，测试连接后保存。
4. 打开任意网页，点击扩展图标，即可在侧边栏看到页面上下文计数，输入“Summarize this page”测试。