## 它是什么

Agent-Native 是一个 TypeScript 全栈框架，核心理念是“动作（Action）定义一次，处处可用”。开发者用 Zod 描述输入，只需编写一段业务逻辑，它就能同时暴露给 UI 按钮、Agent 对话、HTTP API、MCP 服务、A2A 协议和 CLI。框架集成了完整的 Agent 运行时（对话、工具调用、技能、记忆、任务、交接等）和 Drizzle 驱动的 SQL 状态存储，并配套六个可克隆的完整 SaaS 模板。

## 为什么火

当前 AI Agent 开发常陷入“聊天窗口强、融入产品弱”的困境。Agent-Native 将 Agent 做成应用的一等公民：人类和 Agent 共享同一套动作和状态，Agent 能感知用户正在看什么，并像真人协作者一样操作 UI、调用其他 Agent。最近火热的编码 Agent 可视化规划功能（`/visual-plan`/`/visual-recap`）可直接注入现有开发环境，大大降低高阶 Agent 能力的接入成本。

## 技术栈

- **语言**：TypeScript
- **后端**：Nitro 服务器（兼容 Vercel、Netlify、Node 等）
- **数据库**：Drizzle ORM + 任意 SQL 数据库（PostgreSQL、SQLite 等）
- **前端**：React（通过模板可见），使用 Builder.io 组件库
- **Agent 协议**：MCP、A2A（Agent-to-Agent）
- **包结构**：`@agent-native/core`、`@agent-native/skills` 等

## 核心能力

1. **统一动作原语**：`defineAction` 一次定义，UI、Agent、HTTP API、MCP、A2A、CLI 六端复用。
2. **内建 Agent 运行时**：对话管理、记忆（SQL 状态）、技能扩展、定时任务、可观察性、Agent 间交接。
3. **实时人机协同**：数据库状态双向即时同步，Agent 可看见用户高亮内容（Cmd+I），支持多 Agent 交互。
4. **模板生态**：提供 Clips（录屏+日志修复）、Plans（可视化编码规划）、Design（HTML 原型）、Content（本地 MDX 编辑）、Slides（幻灯片生成）、Analytics（看板）六个开箱即用的 SaaS 应用，可独立或组合克隆。
5. **技能注入**：`npx @agent-native/core skills add` 可为 Claude Code、Cursor 等现有编码 Agent 追加可视化规划与回顾命令。
6. **渐进式启动**：支持 Chat 模式（带轻量 UI）、Headless 模式（纯 API/CLI）和完整模板三种起点。

## 适用场景

- 需要 Agent 深入参与业务流程的 SaaS 产品（客服、设计协作、数据洞察）
- 想快速交付智能功能的团队（直接克隆模板二次开发）
- 为已有编码 Agent 补充结构化规划与复盘的中大型团队
- 追求“自进化”应用，让 Agent 直接修改 UI 或业务逻辑的探索性项目

## 同类对比

- vs **LangChain / CrewAI**：后者是后端 Agent 编排库，Agent-Native 则是从接口、UI 到数据库的全套架构，更偏向产品化，而非仅 Agent 逻辑。
- vs **Vercel AI SDK / CopilotKit**：它们提供聊天组件和前端 AI 交互，Agent-Native 则通过 Action 共享让 Agent 与 UI 完全同权，模板更完整。
- vs **OpenAgents / GPT Engineer**：前者多为聊天式代码或任务代理，Agent-Native 额外提供了对业务状态、实时协同和可视化规划的原生支持。

当前项目尚在早期（0.x 版本，Star 2776），生态规模较小，但核心设计理念差异化明确。

## 版本动态

- 最新 Release：`@agent-native/skills@0.2.153`（2026-06-28），为 Patch 更新，依赖 `@agent-native/core@0.79.25`。
- 首次提交：2026-03-12，项目仅三个多月，迭代活跃。
- 文档量：主站文档位于 agent-native.com，仓库内仅提供 `auth.md` 和 `neon-netlify-integration.md`，表明当前重点在认证和无服务器数据库集成。
- 许可：MIT，全部开源。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供与同类框架的性能对比或并发处理基准；自托管完整部署步骤（数据库配置、环境变量）未在 README 中详述；A2A 协议的具体实现规范和兼容性未说明；是否支持自定义 LLM 提供商或本地模型的接入细节待确认；未说明是否支持流式响应（streaming）及多租户隔离方案