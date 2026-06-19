## 安装
Superpowers 是为编码代理设计的技能包，需在目标代理中安装对应的插件。

以 Claude Code 为例：
1. 在 Claude Code 会话中运行 `/plugin install superpowers@claude-plugins-official`（来自 Anthropic 官方市场）。
2. 或使用第三方市场：`/plugin marketplace add obra/superpowers-marketplace` 然后 `/plugin install superpowers@superpowers-marketplace`。

其他代理安装方式见 README（如 Codex CLI 输入 `/plugins` 搜索 Superpowers，Cursor 输入 `/add-plugin superpowers`，Gemini CLI：`gemini extensions install https://github.com/obra/superpowers`，等等）。

## 最小可用示例
1. **启动代理**（安装 Superpowers 后）并描述你要构建的功能，例如：“我想做一个能在 Markdown 中自动修正拼写的 CLI 工具。”
2. 代理会自动触发**brainstorming**技能，提出一系列问题以明确设计，生成设计文档并等待你批准。
3. 批准设计后，代理创建 git worktree 分支，运行测试确认基线的干净。
4. 自动进入**writing-plans**，将设计分解为若干 2-5 分钟任务。
5. 你说“开始”或“go”，代理启动**subagent-driven-development**：逐个任务由新子代理实现，完成后自动进行两阶段审查，通过则继续下一任务，否则修正。
6. 所有任务完成后，**finishing-a-development-branch** 技能验证全部测试通过，询问你是否合并分支或创建 PR。

## 依赖前提
- 本地安装目标编码代理（Claude Code、Codex CLI、Cursor 等）。
- 项目使用 Git 初始化（需要工作树和分支能力）。
- 可选：项目已有测试套件（遵循 TDD 要求，否则技能会引导你添加）。
- 无需额外安装 Superpowers 本身（所谓安装即集成到代理中）。