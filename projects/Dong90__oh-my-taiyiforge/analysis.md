## 它是什么
TaiyiForge（太一炉）是一个 AI 工作流自动化插件，面向严肃使用 AI 做项目的团队。它把 Harness、OpenSpec、GStack、Superpowers、OMO、Spec-Kit 六套工程标准编排成一个状态机，提供九阶段研发主流程（从需求、设计、开发到测试、审查、集成），并通过人类门控和引擎自动校验来保证质量。核心交互方式是一组跨 Claude、Codex、Cursor、OpenCode 四端一致的 slash 命令（v28 共 28 条），让开发者无需记忆阶段顺序或工具差异。

## 为什么火
1. **统一多端体验**：同一套 Skill 和命令在四款主流 AI 编码工具中行为一致，降低团队学习成本。
2. **解决真实痛点**：长会话上下文爆炸、Agent 跳阶段写代码、小修复被迫走全流程等问题都有针对性设计（如令牌精简、复杂度推荐、条件跳过）。
3. **工程化门控**：关键阶段要求 `--approver` 人类确认，自动生成审计日志 `activity.jsonl`，满足严肃交付的可追溯性需求。
4. **轻量零安装**：支持 `npx taiyi-forge-install --all` 一键部署，无需克隆仓库。

## 技术栈
- 主要语言：TypeScript
- 运行环境：Node ≥20
- 架构模式：聊天轨（slash 命令）+ 引擎轨（CLI 校验/门控）+ MCP（只读排障）
- 集成目标：Claude Code、Codex、Cursor、OpenCode
- 测试：Vitest、Playwright（端到端冒烟）
- 工件格式：Markdown 文档驱动，`.taiyi/changes/<slug>/` 作为真源

## 核心能力
- **九阶段流水线**：change → requirement → design → ui-design → task → dev → test → review → integration，每个阶段生成标准工件。
- **28 条跨平台斜杠命令**：覆盖主链（new/status/write/continue）、会话管理、排障、交付、路由、捷径及 6 个伞形命令组（token、test、review、diagram、mode、workflow）。
- **智能状态与引导**：`/taiyi:status` 返回当前阶段、推荐 Skill、下一步动作，`/taiyi:new` 自动创建 slug 并引导填写 CHANGE.md。
- **复杂度自适应**：根据变更复杂度推荐 profile，低复杂度可放宽 quality gate，小修复可走 lite 路径。
- **跨会话续接**：支持 pause/resume，累积上下文 phase-context.ts，避免上下文丢失。
- **门控与审计**：人类门控（change/design/review）强制审批，全流程生成 activity.jsonl 审计日志，交付前 audit 校验。
- **Token 优化**：new/continue 指令从 50 行精简到 1 行，长会话支持 token compress 生成 CONTEXT-COMPACT.md。

## 适用场景
- 使用 AI 编码（Claude/Codex/Cursor）的研发团队，希望规范化需求→交付流程。
- 需要多端统一工作流，避免按工具重新培训。
- 追求严肃交付质量，需要可追溯的决策记录和人工审批节点。
- 已有部分标准化资产（如 Superpowers、OpenSpec），希望编排成一条龙。

## 同类对比
区别于单一的 AI 编码助手或 prompt 框架，TaiyiForge 定位为“编排器”而非新标准创造者。它不替代 Harness、OpenSpec 等已有规范，而是将其组合成可执行的状态机。与直接使用 `spec-kit` 或 `open-spec` 相比，它提供：统一的跨工具命令界面、自动阶段推进与门控、会话续接、以及人类审批集成。比零散的 Skills 组合更系统，比全流程平台更轻量。

## 版本动态
最新 v0.28.1（2026-06-22）主要修复 CI 问题（Playwright 安装、vitest 超时、覆盖率容错）。v0.28.0 带来多项核心优化：复杂度推荐、auto-approver 配置、条件跳过 UI 设计、智能状态显示（具体命令+耗时）、低复杂度质量门放宽、审计日志、累积上下文、仪表板增强、令牌大幅精简等。项目活跃度高，Star 数 413，持续演进中。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供性能基准数据（如大型项目下的阶段执行耗时）；未能说明铁三角（Harness/OpenSpec/GStack 等）的具体集成深度和版本兼容性；未提及多语言支持现状（README 双语但工具本身是否支持国际化）；同类工具横向对比细节有限，仅在方案理念中提及编排对象