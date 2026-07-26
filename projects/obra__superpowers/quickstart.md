## 安装

以 Claude Code 为例：
```bash
/plugin install superpowers@claude-plugins-official
```

其他代理（Cursor、Codex、Gemini CLI 等）的安装命令见仓库 README 的对应平台片段。

## 最小可用示例

1. 启动安装了 Superpowers 的编码代理。
2. 输入一个模糊的需求，例如：“创建一个命令行工具来统计项目中的 TODO 注释”。
3. 代理将自动触发 brainstorming，引导你明确设计、生成 spec，并等待你批准。
4. 批准后，代理生成实现计划，再次等待批准。
5. 然后代理会执行子代理驱动的 TDD 流程，自动提交代码，最终展示合并/PR 选项。

## 依赖前提

- 一个受支持的编码代理（列表见 README 的 Quickstart 部分）
- Git（因 workflow 依赖 git worktree 和分支管理）
- 代理的插件/扩展功能可用（某些代理需先注册市场）