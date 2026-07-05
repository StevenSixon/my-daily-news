## 安装
1. 从 [Releases](https://github.com/alchaincyf/fanbox/releases/latest) 下载适用于 Apple Silicon 的 `.dmg`（或 Intel 版本的 `x64.dmg`）。
2. 将 FanBox 拖入「应用程序」文件夹，双击打开（若提示未验证开发者，右键 → 打开）。

## 最小可用示例
1. 启动 FanBox，默认显示文件侧栏、终端区域。
2. 使用 `⌘K` 搜索本地项目文件夹，回车打开。
3. 在终端中直接键入 `claude` 启动 Claude Code（需预先安装），执行 coding 任务。
4. 观察文件列表：agent 写入的文件会泛起涟漪，点亮卡片。
5. 点击文件卡片可在中间预览区查看内容；点击「跟随模式」则自动跟踪 agent 正在编辑的文件。
6. 拖拽文件或文件夹到终端即插入路径供 agent 使用。

## 依赖前提
- macOS 操作系统（Apple Silicon 或 Intel）
- 若使用 coding agent，需预先安装 Claude Code、Codex 或其他支持的 CLI（FanBox 内置安装命令复制）。
- 终端功能依赖 node-pty，已由 Electron 打包，用户无需额外安装 Node.js。
- 首次打开可能需网络进行 Apple 公证检查，之后离线可用。