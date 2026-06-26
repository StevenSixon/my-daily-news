## 安装
从 [onorca.dev/download](https://onorca.dev/download) 下载对应操作系统的安装包，安装并启动。移动端可从 App Store 或 TestFlight/APK 获取。

## 依赖前提
至少安装一种 CLI 编码代理（如 `claude-code`、`codex`），并拥有有效的 API 订阅。确保代理命令在系统 PATH 中可用。

## 最小可用示例
1. 启动 Orca，点击“+”创建新 Worktree，选择本地 git 仓库。
2. 在终端分屏中运行代理 CLI，例如 `claude` 或 `codex`。
3. 通过快捷键或菜单将同一提示发送到多个 worktree，观察各代理输出。
4. 使用 Diff 视图比较结果，标注反馈，合并最佳代码。
5. 安装移动端 App 接收代理完成的通知，随时发送跟进指令。