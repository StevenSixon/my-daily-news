**安装**
1. 访问 [onOrca.dev/download](https://onorca.dev/download) 下载对应平台（macOS/Windows/Linux）的桌面安装包。
2. 移动端：iOS 从 App Store 获取（或 TestFlight 预览），Android 从 [GitHub Release](https://github.com/stablyai/orca/releases/download/mobile-android-v0.0.22/app-release.apk) 下载 APK。

**前提依赖**
- 系统已安装 git，并配置好 SSH 密钥（如需远程 worktree）。
- 安装至少一个受支持的 CLI Agent（如 `claude`、`codex`）并配置好 API Key/认证。

**最小示例**
1. 启动 Orca 桌面端，首次运行可能要求登录账户或配置 Agent 路径。
2. 在左侧导航栏点击 “Worktrees” → “Create New”，选择一个仓库和一个 Agent 模板。
3. 输入 Prompt：“在 src/utils 下添加一个日志工具模块”，点击启动。
4. 如需并行，在同一个仓库下创建多个 worktree 并分配不同 Agent，发送相同 Prompt。
5. Agent 运行期间可在终端面板观察输出，完成后在 diff 视图对比结果，选择保留的分支合并。
6. 移动端通过扫码或账户同步连接，接收完成通知并查看终端输出。