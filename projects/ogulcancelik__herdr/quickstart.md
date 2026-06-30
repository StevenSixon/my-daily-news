## 安装
支持多种方式，推荐：
```bash
curl -fsSL https://herdr.dev/install.sh | sh
```
或使用包管理器：
```bash
brew install herdr      # macOS
mise use -g herdr       # 通用
nix run github:ogulcancelik/herdr   # Nix
```

## 最小可用示例
1. 在终端启动 herdr：
```bash
herdr
```
这会启动后台服务器并打开一个工作区。

2. 在默认面板中运行一个代理，例如 Claude Code：
```bash
claude
```
3. 按 `ctrl+b` 然后按 `v` 垂直分割面板，再运行另一个代理如 Codex：
```bash
codex
```
4. 此时左侧边栏会自动显示每个代理的状态（阻塞/工作中/完成），无需额外配置。

5. 断开而不终止代理：按 `ctrl+b` 然后按 `q` 退出客户端。代理继续在后台运行。稍后执行 `herdr` 重新连接，所有会话保持原样。

## 远程连接示例
在远程机器上启动 herdr，本地通过 SSH 连接：
```bash
herdr --remote workbox               # 假设 workbox 是 ~/.ssh/config 中的主机别名
herdr --remote ssh://you@server:2222 # 直接指定
```

## 依赖前提
- 无需任何外部运行时或依赖，Rust 编译的单文件即可启动。
- 需要 Linux/macOS 终端环境（Windows 为 beta 功能，可能不完全稳定）。
- 远程功能需要 SSH 客户端并配置好主机访问。