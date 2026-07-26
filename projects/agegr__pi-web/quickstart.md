**依赖**：Node.js ≥ 22.19.0，本地已安装 pi 代理 (`~/.pi/agent/sessions` 存在)。

**快速启动**：
```bash
npx @agegr/pi-web@latest
```
或全局安装：
```bash
npm install -g @agegr/pi-web
pi-web
```
浏览器自动打开 (若无则访问 `http://127.0.0.1:30141`)。

**自定义选项**：
```bash
pi-web --port 8080 --hostname 0.0.0.0   # 仅限可信网络
PORT=8080 PI_WEB_HOSTNAME=0.0.0.0 pi-web  # 环境变量方式
```
**注意**：没有内置认证，绝对不要暴露到互联网。