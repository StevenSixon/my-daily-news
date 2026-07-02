## 安装
1. 访问 [onorca.dev/download](https://onorca.dev/download) 下载对应平台的桌面应用。
2. 移动端可从 [iOS App Store](https://apps.apple.com/us/app/orca-ide/id6766130217) / [Android APK](https://github.com/stablyai/orca/releases/download/mobile-android-v0.0.18/app-release.apk) 获取。

## 最小可用示例
1. 确保已安装至少一个 CLI 编码代理（例如 `npm install -g @anthropic-ai/claude-code` 并配置 API key）。
2. 在 Orca 中打开一个工作区，创建新 Worktree，选择代理（如“Claude Code”），输入 prompt：“实现一个简单 Todo REST API”。
3. 重复步骤 2，选择另一个代理（如“Codex”），使用相同 prompt。
4. 两个代理将在各自的隔离环境中运行，终端实时显示输出；完成后通过“AI Diffs”对比结果，选择最优实现合并。
5. 手机端可随时打开 Orca 查看运行状态，任务结束会收到推送通知。

## 前提
- 运行代理所需的 API key/订阅（由用户自行提供）
- 操作系统：macOS, Windows, Linux 均支持
- Git 已安装且配置