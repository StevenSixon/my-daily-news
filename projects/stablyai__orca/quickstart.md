## 安装

- 桌面端：从 [onorca.dev/download](https://onorca.dev/download) 获取 macOS/Windows/Linux 安装包。
- 移动端：iOS 从 App Store 或 TestFlight 下载；Android 从 [GitHub Releases 下载 APK](https://github.com/stablyai/orca/releases/download/mobile-android-v0.0.21/app-release.apk)。

## 最小可用示例

1. 打开 Orca，登录你的 GitHub 账户（用来创建工作树）。
2. 在终端中确保已安装某个 AI 编码代理，例如 `npm install -g @anthropic-ai/claude-code`。
3. 在 Orca 中创建一个新工作树（关联某个仓库），然后在此工作树的面板中打开终端，直接运行 `claude` 或其他代理命令。
4. 也可通过 `Cmd+J` 快速搜索并打开已有工作树。
5. 从 GitHub 或 Linear 任务页面点击“打开工作树”，Orca 自动创建隔离分支并分配代理。

## 依赖前提

- 需要本地安装所选 CLI 代理（Claude Code、Codex 等）并配置好 API 密钥。
- 使用 Git 仓库才能创建独立的工作树。
- 移动端配合需要桌面端运行中并关联同一账户。