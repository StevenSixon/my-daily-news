## 它是什么
Deer Workflow 是一个**图工程 (Graph Engineering) 运行时**：你用 TypeScript 描述工作流的分支、并行、错误处理（控制平面），将具体的语义工作（如“研究这个主题”）委托给可替换的 Coding Agent（执行平面）。默认 Agent 是 OpenAI Codex CLI，也内置了 Claude Code，接口保持厂商中立。

## 为什么火
当前 Agent 编排大多依赖对话或低代码拖拽，流程不透明、难复现。Deer Workflow 把控制流写进代码，版本化、可审查，把“怎么跑”和“谁来跑”解耦。对需要可靠、可维护 Agent 流水线的开发者吸引力很大。它还是字节跳动 DeerFlow 3.0 的试点，自然受关注。

## 技术栈
- 语言：TypeScript
- 运行时：Bun（推荐）；npm 包可发布
- 默认 Agent：OpenAI Codex CLI
- 内置 Agent：Claude Code CLI
- 可观测：终端 TUI + JSONL 事件流
- 生成能力：内置 `workflow-creator` 技能，从自然语言生成工作流模块

## 核心能力
- **代码即计划**：TypeScript 定义阶段、输入、错误处理，不是 Agent 的临时对话。
- **Agent 可替换**：Codex、Claude 即装即用，公共接口允许接入其他 Coding Agent。
- **全链路可观测**：交互模式有分阶段 TUI；自动化模式输出稳定 JSONL 事件流，可接 CI/服务器。
- **从描述到运行**：一行命令从需求生成可执行的工作流 TypeScript 文件，直接运行。

## 适用场景
- 深度研究：并行搜集、验证、合成报告（仓库自带示例 `deep-research`）
- 内容生成流水线：规划、撰写、审核结构化输出（`blog-writer` 示例）
- 任何需要多步骤、可审查、可复用的 AI 自动化任务

## 同类对比
- vs **LangGraph**：LangGraph 用代码构建状态图，但 Agent 节点通常由开发者用 LangChain 工具实现。Deer Workflow 更激进：节点工作完全交给外部 Coding Agent，自己只负责编排。
- vs **CrewAI / Dify**：低代码/对话式定义流程，易用但过程不透明；Deer Workflow 是 code-first，强调可审查和版本控制。
- 不足：项目极新（v0.2.0），生态尚未成型，目前仅两个官方示例，社区规模小。

## 版本动态
- 2026-07-27 发布 v0.2.0，加入 ClaudeAgent（Claude Code CLI 运行时）。
- 2026-07-26 仓库创建，随后迅速推出 v0.1.0。
- 当前 Star 244，开发活跃，每日有推送。
---

## ℹ️ 置信度与信息盲区

- 置信度：**medium**
- 信息盲区：未提供性能基准数据（如执行延迟、并行吞吐）；未说明是否支持 Bun 之外的 Node.js 运行时，或是否有额外依赖；未给出与 LangGraph、CrewAI 等的量化对比或迁移指南；docs/api.md 内容未在上下文中，API 完整度未知；仅两个示例，未覆盖复杂错误恢复、人工审批等模式