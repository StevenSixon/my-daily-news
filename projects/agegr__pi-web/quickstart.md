## 安装与启动
### 前提
- Node.js >= 22.19.0
- 本地已安装并配置过 [pi coding agent](https://github.com/badlogic/pi-mono)

### 临时运行
```bash
npx @agegr/pi-web@latest
```
服务运行在 `http://127.0.0.1:30141`，浏览器会自动打开。

### 全局安装
```bash
npm install -g @agegr/pi-web
pi-web
```

### 常用选项
```bash
pi-web --port 8080              # 自定义端口
pi-web --hostname 0.0.0.0       # 在受信网络上暴露服务
pi-web --no-open                # 禁止自动打开浏览器
```
支持环境变量 `PORT`、`PI_WEB_HOSTNAME`、`PI_WEB_ALLOWED_HOSTS` 和 `PI_WEB_NO_OPEN`。

### 代理配置
读取标准环境变量 `HTTP_PROXY`、`HTTPS_PROXY`、`NO_PROXY` 为模型和 API 请求提供服务端代理。

## 最小可用示例
1. 确保 pi agent 已生成过至少一个会话文件（位于 `~/.pi/agent/sessions`）
2. 启动 pi-web
3. 在侧边栏选择一个项目，即可看到历史会话列表
4. 点击会话进行浏览，或在聊天框输入新消息开始与 agent 交互