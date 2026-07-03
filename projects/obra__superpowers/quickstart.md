## 安装
根据你使用的编码代理选择一种安装方式：

**Claude Code**（官方市场）：
```bash
/plugin install superpowers@claude-plugins-official
```

**Cursor**：
在 Agent 聊天中输入 `/add-plugin superpowers`。

**Codex App**：在插件侧边栏搜索 Superpowers 并点击添加。

**GitHub Copilot CLI**：
```bash
copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace
```

其他工具（Antigravity、Factory Droid、Kimi Code、OpenCode、Pi）参见 [README](https://github.com/obra/superpowers)。

## 最小可用示例
安装后，在代理中开始一个新对话，描述你要开发的功能，如：
> 我想给现有的 REST API 添加一个速率限制中间件

代理会自动进入 brainstorming 阶段，不会立即写代码，而是反问你设计细节。确认设计后，会生成规划并询问是否开始实现。回答“go”后，它会创建独立工作分支，逐个任务进行 TDD 开发，并子代理审查。

## 依赖前提
- 你需要拥有对应编码代理的可用环境（Claude Code、Cursor 等）
- 项目必须是已有的代码仓库，以便使用 Git worktree 特性（可选但推荐）
- 无需额外安装语言运行时，技能为纯文本指令