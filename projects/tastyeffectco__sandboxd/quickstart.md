## 前提
- Linux 主机，安装 Docker Engine 和 Docker Compose 插件。
- 克隆仓库。

## 安装
```bash
git clone https://github.com/tastyeffectco/sandboxd.git
cd sandboxd
./install.sh
```
脚本会检查 Docker、生成 `.env`、构建基础镜像和控制平面，启动后 API 在 `http://127.0.0.1:9090`。

## 最小可用示例
```bash
API=http://127.0.0.1:9090
# 创建沙箱（开放 3000 端口）
ID=$(curl -s -XPOST $API/sandbox -H 'content-type: application/json' \
       -d '{"ports":[3000]}' | sed -E 's/.*"id":"([^"]+)".*/\1/')
# 提交任务让 OpenCode 代理构建应用
TASK=$(curl -s -XPOST $API/v1/sandboxes/$ID/tasks -H 'content-type: application/json' -d '{
        "prompt":"create a Vite todo app and run on port 3000",
        "agent":"opencode"
     }')
# 流式获取代理输出
curl -N $API/v1/sandboxes/$ID/tasks/<taskId>/events
# 打开预览：http://s-<id>-3000.preview.localhost
```
使用 API 密钥时在创建沙箱时传入 `env` 对象。