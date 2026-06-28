### 安装
1. 从 [Releases 页面](https://github.com/alchaincyf/fanbox/releases/latest) 下载最新的 `.dmg` 文件。
2. 将应用拖入“应用程序”文件夹。
3. 首次打开时若 macOS 提示“未验证的开发者”，请右键点击应用图标 → 打开 → 确认，即可运行。

### 最小可用示例
1. 启动 FanBox，使用 ⌘K 打开模糊搜索，输入项目名片段，选择文件夹以加载文件树。
2. 在右侧或下方的内嵌终端中键入 `claude` 或 `codex` 开始 agent 会话。
3. 拖拽文件到终端以插入路径作为上下文；点击终端输出中的文件路径可在 FanBox 内直接预览。
4. 当 agent 创建或修改文件时，左侧卡片会出现涟漪动画，点击跟随按钮可实时追踪当前编辑的文件。

### 依赖前提
- **系统**：macOS（Apple Silicon 原生支持，Intel Mac 未提供官方构建）
- **Agent**：需自行安装 Claude Code 或 Codex CLI 工具并在 PATH 中可用
- 应用本身零运行时依赖，无需 Node.js 或额外配置