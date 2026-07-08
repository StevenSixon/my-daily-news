## 安装
- **桌面端**：从 [onorca.dev/download](https://onorca.dev/download) 获取 macOS、Windows 或 Linux 安装包，也可直接下载最新 [Release](https://github.com/stablyai/orca/releases) 中的安装文件。
- **移动端**：iOS 可通过 [App Store](https://apps.apple.com/us/app/orca-ide/id6766130217) 或 TestFlight 安装；Android 下载 [APK 0.0.24](https://github.com/stablyai/orca/releases/download/mobile-android-v0.0.24/app-release.apk)。

## 前提依赖
- 已安装并使用任一 CLI 代理（如 `claude`、`codex`、`opencode`、`pi`），确保其在终端可直接运行并已配置有效订阅/密钥。
- Git 环境可用（用于 worktree 隔离）。

## 最小可用示例
1. 启动 Orca，打开一个仓库（或克隆新仓库）。
2. 在侧边栏创建新 Worktree，选择「Parallel」模式。
3. 输入提示词，选择要并行运行的代理（点击加号添加多个）。
4. 点击运行，每个代理将在独立终端中执行，各自的文件变更隔离在分支中。
5. 在 Diff 视图中对比结果，选择接受或合并，然后提交。

## 高级提示
- 使用 `Cmd/Ctrl+J` 快速搜索并切换标签页/会话。
- 通过 Orca CLI（`orca worktree create` 等）可在外部脚本中自动化上述流程。
- 移动端配对：登录同一账户，即可在手机上查看代理输出并发送新消息。