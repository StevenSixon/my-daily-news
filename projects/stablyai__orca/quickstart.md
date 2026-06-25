## 安装
- 从 [官网](https://onorca.dev/download) 下载对应平台（macOS/Windows/Linux）的桌面应用。
- 移动端：iOS 通过 App Store 或 TestFlight 安装；Android 下载 [APK](https://github.com/stablyai/orca/releases/download/mobile-android-v0.0.16/app-release.apk)。

## 最小使用示例
1. 启动 Orca，配置你希望使用的 AI 代理的 API 密钥或 CLI 工具（例如安装 `claude`、`codex` 命令行）。
2. 在 Orca 中打开一个 Git 仓库，点击创建新的工作树（worktree），选择代理并输入 prompt。
3. 可同时创建多个工作树，分配不同 prompt 或不同代理，观察实时输出，通过 diff 视图对比结果。
4. 使用拖放或设计模式快速提供代码上下文给代理。

## 依赖前提
- 需要在系统上安装对应的 AI 代理 CLI 工具（如 Anthropic 的 `claude`、OpenAI 的 `codex` 等）并配置好认证。
- Git 仓库支持 `git worktree` 功能。