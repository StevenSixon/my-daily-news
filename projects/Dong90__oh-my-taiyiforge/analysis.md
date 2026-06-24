## 它是什么
TaiyiForge 是一款 AI 编码工作流自动化插件，将 AI 辅助开发过程从“玄学对话”改造为由状态机驱动的九阶段工程流水线。每个阶段有固定产出和审批点，强制人类在关键决策点介入，确保 AI 不跳过需求、设计或审查。它通过一套统一的 slash 命令，在 Claude、Codex、Cursor、OpenCode 四个 AI 终端中提供一致的行为。

## 为什么火
仓库创建仅 3 周即获 492 星，切中了团队使用 AI 编码的普遍痛点：Agent 总是跳过设计直接写代码、长会话上下文丢失、不同工具流程各异。它给出了一套可落地、可复制的纪律框架，将“AI 写代码”提升到“AI 工程化”，因此吸引关注。

## 技术栈
TypeScript + Node.js (≥20)，通过 npm 包 `oh-my-taiyiforge` 分发。核心包含状态机引擎、事件总线、ChangeGraph 知识图谱、token 压缩机制及结构化日志。集成到 AI 终端依靠 slash 命令与 SKILL.md 声明。

## 核心能力
- **九阶段流水线**：change → requirement → design → ui-design → task → dev → test → review → integration，每步有明确工件。
- **人类门控**：change、design、review 三个关键阶段必须人类审批，引擎不理会 AI 的自我放行。
- **多端一致**：28 条 slash 命令及 6 个 umbrella 功能在四端行为完全对齐。
- **强制 TDD**：dev 阶段必须先写失败的测试再实现，不是建议是硬约束。
- **证据防假过门**：每个验收标准必须附可执行验证命令（evidence），跑不过不进入下一阶段。
- **Token 压缩与断点续传**：长会话自动产出 CONTEXT-COMPACT.md，跨天无缝继续。
- **ChangeGraph**：追踪变更间依赖，改一处知全局。
- **灵活 profile**：full（大功能）、lite（小修复）、nano（typo 改）等 10 种模式。

## 适用场景
- 要求 AI 辅助编码有纪律、可审计的团队。
- 同时使用多个 AI 编码工具，需要统一流程。
- 需要将 AI 生成的代码置于强制设计、审查和测试门控下的项目。

## 同类对比
直接与裸 AI 对话相比，TaiyiForge 提供了严格的流程控制和审批，但 README 未展开与同生态工具（Harness、OpenSpec、Superpowers 等）的横向对比，仅声明编排了它们的思想。

## 版本动态
最新 v0.42.0 聚焦文档与工程基建（README 精炼、CI 自动发布）。核心功能在 v0.23–v0.40 期间建立：规范命令集、evidence 强校验、事件总线、ChangeGraph 等。v1.0.0 计划锁定 API、达成四端 parity 并开始收集外部案例。
---

## ℹ️ 置信度与信息盲区

- 置信度：**medium**
- 信息盲区：无性能 benchmark 或 token 压缩的量化效果数据；多 AI 终端行为一致性的验证报告缺失；缺乏生产环境下的稳定性数据和用户案例；人类门控的具体实现机制未说明（是否仅依赖聊天层面的确认）；除 Node.js ≥20 外未列出其他系统依赖（如操作系统、额外工具）