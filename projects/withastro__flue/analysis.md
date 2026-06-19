## 它是什么
Flue 是一个 Agent Harness 框架，不是传统的 LLM SDK。它为 TypeScript 提供了一整套可编程的“挽具”：沙箱环境、工具、技能、会话管理、工作流编排和持久执行。目标是让开发者能够构建像 Claude Code 或 Codex 那样的自主代理——给定一个任务，代理可以自主地使用工具、修改文件、跨会话保持上下文，并在安全的沙箱中完成真实工作。

## 为什么火
近年来，Claude Code 等产品展示了真正自主代理的威力，但实现这样的架构需要一套复杂的运行时。Flue 提炼了这种模式，提供开箱即用的 harness，使普通团队也能复现这种代理能力。它填补了从 LLM SDK 到完整自主代理之间的鸿沟，尤其适合需要安全沙箱、多工具协调和持久状态的企业场景。5714 颗星表明社区对此方向的高度关注。

## 技术栈
- 语言：TypeScript
- 核心包：`@flue/runtime`（运行时）、`@flue/cli`（构建工具）、`@flue/sdk`（客户端）、`@flue/opentelemetry`（遥测）、`@flue/postgres`（持久化）
- 沙箱支持：本地（`local()`）、虚拟容器、远程容器（如 Daytona）
- 模型：示例中使用 Anthropic Claude Sonnet，但支持多种模型（未完整列出）
- 部署目标：Node.js、Cloudflare Workers、GitHub Actions、GitLab CI/CD、Render 等
- 集成：MCP 服务器、Slack/Discord/Teams 等多渠道

## 核心能力
- **代理与工作流**：构建保持上下文的自主代理，同时也支持结构化工作流。
- **沙箱执行**：为代理提供隔离的文件系统和代码执行环境，确保安全。
- **持久执行**：通过 Durable Execution 自动处理故障和重试，代理进度不会丢失。
- **工具与技能**：类型安全的工具调用和可复用的技能包（如 bug 分诊、验证），代理可按需加载。
- **子代理委派**：可定义专家角色，主代理能将子任务委派给子代理。
- **MCP 兼容**：连接 Model Context Protocol 生态的工具和服务。
- **可观测性**：内置 OpenTelemetry 跟踪、Braintrust/Sentry 集成，也支持自定义观察器。
- **多渠道接入**：从 Slack、Teams、Discord、GitHub 等渠道接收事件，统一处理。

## 适用场景
- 自动化客服与工单处理（通过 Slack/Discord/邮件等渠道）
- 软件工程助手：bug 复现、诊断、修复等端到端任务
- 多步骤业务工作流自动化，需要代理根据环境做决策
- 在安全沙箱中执行不可信代码或未验证的工具调用

## 同类对比
与 LangGraph、CrewAI、AutoGen 相比，Flue 更强调“Harness”理念，它不是单纯的任务链或对话编排，而是为代理提供一个完整的、可编程的执行环境（沙箱、持久性、工具/Skill 系统），更贴近 Claude Code 的内部架构。其 TypeScript 原生支持和多渠道适配在侧重 JavaScript/TypeScript 技术栈的团队中优势明显。

## 版本动态
仓库创建于 2026-02-07，最新推送 2026-06-19，处于快速迭代期。Star 数已达 5714，生态活跃。

---

## ℹ️ 置信度与信息盲区

- 置信度：**medium**
- 信息盲区：未提供完整的安装步骤和系统依赖（如是否依赖 Docker 作为沙箱）；未列出支持的 AI 模型完整列表，示例仅提及 Claude Sonnet；未给出持久执行和子代理的具体代码示例；未说明部署到 Cloudflare Workers 等平台的详细限制；无性能基准或规模数据