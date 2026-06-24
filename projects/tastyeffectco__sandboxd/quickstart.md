## 前提
- 带 Docker Engine 及 Compose 插件的 Linux 主机
- 本地开发可用 `*.localhost`（无需 DNS 或证书）

## 安装
```bash
git clone https://github.com/tastyeffectco/sandboxd.git
cd sandboxd
./install.sh
```
`install.sh` 会检查环境、生成 `.env`、构建基础镜像和控制平面，并启动所有服务。API 默认在 `http://127.0.0.1:9090`。

## 最小可用示例
```bash
# 1. 创建沙箱（暴露 3000 端口）
ID=$(curl -s -XPOST http://127.0.0.1:9090/sandbox -H 'content-type: application/json' \
     -d '{"ports":[3000]}' | sed -E 's/.*"id":"([^"]+)".*/\1/')

# 2. 让 AI 代理在里面生成应用
curl -s -XPOST http://127.0.0.1:9090/v1/sandboxes/$ID/tasks \
  -H 'content-type: application/json' \
  -d '{"prompt":"create a Vite app that shows a todo list and run it on port 3000", "agent":"opencode"}'

# 3. 查看代理输出（SSE 流）
curl -N http://127.0.0.1:9090/v1/sandboxes/$ID/tasks/<taskId>/events

# 4. 打开预览 URL（服务启动后）
http://s-<id>-3000.preview.localhost
```
若需使用自己的模型 Key，在创建沙箱时传入环境变量：
```bash
curl -XPOST ... -d '{"ports":[3000], "env":{"ANTHROPIC_API_KEY":"sk-ant-..."}}'
```