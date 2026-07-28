## 安装
**桌面版**：从 [GitHub Releases](https://github.com/penecho/penecho/releases/latest) 下载。

**npm 全局安装**（需 Node.js 20.3+）：
```bash
npm install -g penecho
penecho configure   # 交互式配置LLM源
penecho             # 启动服务，浏览器访问 http://localhost:3888
```
若使用 Codex CLI 或 Claude CLI 模式，需先安装并认证对应 CLI（如 `npm install -g @openai/codex@latest && codex login`）。

**源码启动**：
```bash
git clone <repo-url>
npm install
npm start          # 直接启动
```
默认端口 3888，可通过 `--port` 参数修改。服务启动后会要求浏览器设置六位安全码或开放局域网访问。