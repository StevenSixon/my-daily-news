## 安装

1. 确保已安装 Hermes Agent 并启动网关（`hermes gateway run`）。
2. 克隆仓库：`git clone https://github.com/abundantbeing/hermes-browser-extension && cd hermes-browser-extension`。
3. 安装依赖并构建：`npm install && npm run build`。
4. 打开 `chrome://extensions`，开启开发者模式，点击“加载已解压的扩展程序”，选择项目的 `dist/` 目录。

## 最小可用示例

1. 点击扩展图标打开侧边面板。
2. 点击“Connect to Hermes”，选择“Local gateway”，填入 `http://127.0.0.1:8642` 和 API 密钥（如果本地网关已按文档配置）。
3. 打开任意 `https` 页面，在侧边面板输入：`Summarize this page in one sentence.` 并发送。

## 依赖前提

- Node.js 20+
- Chrome / Edge / Chromium 114+（支持 Side Panel API）
- Hermes Agent 本地或远程可达的 API 服务器（默认端口 8642）