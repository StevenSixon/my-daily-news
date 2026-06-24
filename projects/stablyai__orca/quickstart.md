## 安装
访问 [https://onorca.dev/download](https://onorca.dev/download) 下载对应平台（macOS/Windows/Linux）安装包。桌面应用安装后初次启动可能需要授权终端及文件访问权限。
移动端：iOS 用户前往 App Store 搜索 “Orca IDE”；Android 用户从 [GitHub Release](https://github.com/stablyai/orca/releases) 下载 APK 手动安装。

## 前提依赖
- Git 已安装（worktree 功能依赖）
- 至少一个支持的 CLI Agent（如 Claude Code、Codex 等）需自行安装并配置 API key/订阅
- 远程工作树需要 SSH 客户端及远程主机可访问

## 快速上手
1. 启动 Orca，打开已有仓库或克隆一个新仓库。
2. 在界面中点击“新建 worktree”，选择要运行的 Agent（或者直接在终端中运行 `orca worktree create <agent-name>`）。
3. 输入任务 prompt，Agent 即在隔离工作树中执行；可同时创建多个不同 Agent 的 worktree。
4. 通过终端面板实时观察输出，完成后审查 diff，使用 Diff 注释反馈给 Agent。
5. 合并满意的变更到主分支，删除多余 worktree。

远程使用：配置 SSH 主机后，创建 worktree 时选择远程目标，Agent 便在远程执行，端口转发自动建立。

CLI 高级用法：`orca worktree snapshot` 保存当前状态，`orca click` 模拟点击 UI 元素供 Agent 操作，脚本可全自动编排。