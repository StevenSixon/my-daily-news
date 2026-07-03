## 安装
```bash
curl -fsSL https://raw.githubusercontent.com/omnigent-ai/omnigent/main/scripts/install_oss.sh | sh
```
或手动：`uv tool install omnigent`（需 Python 3.12+，以及 uv、git、Node.js 22+、tmux 等）

## 最小示例
```bash
# 启动默认代理（交互式选择模型）
omnigent

# 启动特定代理
omnigent claude
omnigent codex

# 运行内置多代理示例
omnigent run examples/polly/
omnigent run examples/debby/

# 启动服务器和 Web UI
omnigent server start
omnigent host  # 另一终端注册本机
```
访问 http://localhost:6767 即可从浏览器使用。支持 `/model` 命令切换模型。

## 前提依赖
- Python 3.12+, uv, git, Node.js 22+ (含 npm)
- 对于终端封装的各代理，需安装对应的 CLI 并已认证
- Linux 需 bubblewrap，macOS 无需额外沙箱工具