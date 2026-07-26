**安装**
前往 [官网下载页](https://onorca.dev/download) 获取对应平台安装包，或从 [GitHub Releases](https://github.com/stablyai/orca/releases) 下载桌面版（macOS/Windows/Linux）；移动端可从 iOS App Store 或 Android APK 安装。

**最小示例**
1. 启动 Orca，在设置中配置你想使用的代理 CLI 路径和 API 密钥（使用你自己的订阅）。
2. 点击“New Worktree”，选择目标 git 仓库和代理（如 Claude Code）。
3. 输入任务描述，例如“实现用户登录 API”。
4. 可重复步骤 2-3 创建多个工作树，并分配不同代理。
5. 在移动端同步查看进度，完成后用“Merge the winner”比较并合并最佳分支。

**依赖前提**
- 对应的 CLI 代理需要预先在本地或远程机器上安装（如 `claude`、`codex` 等）。
- 需要这些代理的 API 密钥或订阅账户。
- 远程工作树需要目标机器开启 SSH 访问。