## 快速上手
1. **下载桌面应用**：访问 [https://onorca.dev/download](https://onorca.dev/download) 获取 macOS/Windows/Linux 版，或从源码构建（克隆仓库，`npm install`，`npm run build`，需 Node.js 22+）。
2. **安装 CLI 代理**：确保本地已安装至少一个受支持的编码代理（如 `claude`、`codex`、`opencode` 等），并配置好 API 密钥。
3. **创建工作区**：在 Orca 中打开一个 Git 仓库，点击「New Worktree」，选择代理类型，输入提示词，即可开始并行运行多个代理。
4. **（可选）安装移动端**：iOS 从 App Store 下载，Android 使用 [APK](https://github.com/stablyai/orca/releases/download/mobile-android-v0.0.17/app-release.apk)，登录相同账户后即可远程监控和操作。

**最小可用示例**：在一个 Node.js 项目中，同时让 Claude Code 和 Codex 修复一个 bug，在 Orca 中对比两个 worktree 的 diff，选择最优解合并回主分支。