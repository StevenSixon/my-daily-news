## 安装
```bash
# 一键安装脚本
curl -fsSL https://raw.githubusercontent.com/omnigent-ai/omnigent/main/scripts/install_oss.sh | sh
# 或使用 uv（需 Python 3.12+）
uv tool install omnigent
# 或 Homebrew
brew install omnigent-ai/tap/omnigent
```
**前提依赖**：`git`、`uv`、Node.js 22+（含 npm）、`tmux`；Linux 还需 `bubblewrap`（`apt install bubblewrap`）。安装脚本会尝试自动配置缺失项。

## 最小可用示例
```bash
# 启动默认 agent
omnigent

# 直接使用特定 agent
omnigent claude
omnigent codex

# 运行自定义 agent（示例项目自带）
omnigent run examples/polly/    # 多 agent 编码 orchestrator
omnigent run examples/debby/    # 双头辩论 agent

# 配置模型
omnigent setup

# 启动服务器并注册本机为 host，通过浏览器使用
omnigent server start
omnigent host
# 访问 http://localhost:6767
```
## 从手机使用
在同一局域网内，手机浏览器访问本机 IP:6767；或部署到云服务器并 `omnigent login https://your-server`，即可跨设备使用。