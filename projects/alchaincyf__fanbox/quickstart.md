## 安装
1. 访问 [Releases](https://github.com/alchaincyf/fanbox/releases/latest) 下载对应架构的 `.dmg`（Apple 芯片选 arm64，Intel 选 x64）。
2. 双击挂载后拖入 `应用程序` 文件夹。
3. 首次打开若提示安全警告，**右键点击 → 打开 → 确认**。

## 最小可用示例
1. 打开 FanBox，点击 `+` 或按 `⌘K` 搜索并打开本地项目文件夹。
2. 在右侧终端区域，点击面板上的 `Claude Code` 或 `Codex` 按钮（如果未安装会提示安装命令）。
3. 输入 agent 指令（如 `创建一个 React 组件`），观察左侧文件列表：agent 修改的文件卡片会亮起呼吸光效。
4. 点击任意文件预览内容，或打开 **跟随模式** 实时观看 agent 编辑的文件和 HTML 渲染。
5. 点击底部状态栏的“回合存档”查看会话历史，随时一键回滚。

## 依赖前提
- macOS 操作系统（Elecron 打包，Apple Silicon 原生，Intel 兼容）
- 无需 Node.js、Python 等运行时，应用内自带终端依赖
- 运行 agent 需对应 CLI 已安装（如 Claude Code、Codex 等），FanBox 会提示安装命令但不会自行安装