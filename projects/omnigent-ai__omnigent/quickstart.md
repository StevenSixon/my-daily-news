## 安装
### 一键安装（推荐）
```bash
curl -fsSL https://raw.githubusercontent.com/omnigent-ai/omnigent/main/scripts/install_oss.sh | sh
```
### 手动安装
- 需要 Python 3.12+
```bash
uv tool install omnigent    # 或者 pip install omnigent
```
或
```bash
brew install omnigent-ai/tap/omnigent
```

## 最小可用示例
启动第一个代理（交互式选择模型）：
```bash
omnigent
```
直接使用特定代理运行时：
```bash
omnigent claude    # Claude Code
omnigent codex     # Codex
omnigent cursor    # Cursor
omnigent opencode  # OpenCode
omnigent hermes    # Hermes
omnigent pi        # Pi
```
运行示例项目：
```bash
omnigent run examples/polly/   # 多代理编码协调员
omnigent run examples/debby/   # 双头头脑风暴伙伴
```

## 依赖前提
- Python 3.12+
- Node.js 22 LTS 及 npm（用于安装各代理 CLI）
- tmux（用于终端原生交互，Windows 无需）
- Linux 需要 bubblewrap 做沙箱隔离
- 模型凭证：至少一个 API key 或配置好的 CLI 登录

详细配置模型与凭证：
```bash
omnigent setup
```
然后根据指引添加 API key、订阅凭证或网关地址。