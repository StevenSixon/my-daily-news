## 安装与上手
1. 访问 [https://onorca.dev/download](https://onorca.dev/download) 下载 macOS、Windows 或 Linux 安装包。
2. 移动端可选：[iOS App Store](https://apps.apple.com/us/app/orca-ide/id6766130217) 或直接下载 [Android APK](https://github.com/stablyai/orca/releases/download/mobile-android-v0.0.17/app-release.apk)。
3. 确保系统已安装 Git 和至少一个受支持的 CLI 代理（如 Claude Code、Codex）。
4. 启动 Orca，在设置中配置你的代理路径和 API 密钥（使用你自己的订阅）。
5. 创建第一个工作树：在界面中点击“New Worktree”或使用 CLI：`orca worktree create --name my-feature`。
6. 在终端中向代理发送提示，或使用 Quick Open 分派任务。浏览器 Design Mode 可按需提取 UI 元素。
7. 在移动设备上登录同一账号，即可实时监控和干预。

**最小示例**：
```bash
# 创建隔离栅
orca worktree create --name experiment-a
orca worktree create --name experiment-b
# 在两个 worktree 中分别启动不同代理
orca agent run --worktree experiment-a claude-code "实现登录页面"
orca agent run --worktree experiment-b codex "实现登录页面"
# 通过 UI 对比 diff，选择更优结果合并
```