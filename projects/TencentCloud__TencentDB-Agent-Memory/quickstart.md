### OpenClaw 快速启用
1. 安装插件：
```bash
openclaw plugins install @tencentdb-agent-memory/memory-tencentdb
openclaw gateway restart
```
2. 修改配置 `~/.openclaw/openclaw.json`：
```jsonc
{
  "memory-tencentdb": {
    "enabled": true
  }
}
```
3. （可选）开启短期上下文压缩：添加 `config.offload.enabled: true`，并注册 `slots.contextEngine: "memory-tencentdb"`。

依赖：Node.js ≥22.16，OpenClaw ≥2026.3.13。

### Hermes Docker 一键部署
```bash
cd docker/opensource
docker build -f Dockerfile.hermes -t hermes-memory .
docker run -d \
  --name hermes-memory \
  --restart unless-stopped \
  -p 8420:8420 \
  -e MODEL_API_KEY="your-api-key" \
  -e MODEL_BASE_URL="https://api.lkeap.cloud.tencent.com/v1" \
  -e MODEL_NAME="deepseek-v3.2" \
  -e MODEL_PROVIDER="custom" \
  -v hermes_data:/opt/data \
  hermes-memory
```
Gateway 监听 8420 端口，数据持久化在命名卷中。