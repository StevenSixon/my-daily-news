## 它是什么

eve 是 Vercel 开源的“文件系统优先”AI 代理框架。它不要求你写冗长的编排代码，而是通过约定的目录结构（`agent/instructions.md`、`agent/tools/`、`agent/skills/` 等）来定义代理的行为。代理的能力直接映射到文件系统，方便审查、扩展和团队协作。

## 为什么火

- 由 Vercel 官方推出，自带生态光环，发布两个多月即获 3.3k+ star。
- 解决了“代理项目逻辑散落、难以维护”的痛点，把提示词、工具、调度等配置实体化为文件，降低了认知负担。
- 内置 TUI (`npx eve init` 后的交互终端) 和本地沙箱，开箱即用，开发体验友好。

## 技术栈

- 语言：TypeScript
- 运行时：Node.js
- 依赖：Zod 用于工具输入校验，支持主流模型（如 Anthropic Claude，示例中为 `claude-sonnet-5`）。
- 部署：可本地运行，推测可部署至 Vercel 或其他 Node 环境。
- 沙箱：`eve eval` 涉及本地沙箱（microsandbox），用于安全执行。

## 核心能力

- **约定式项目结构**：`agent/` 目录下分 `instructions.md`（系统提示）、`tools/`（类型化函数）、`skills/`（按需加载的过程）、`channels/`（消息通道，如 Slack、Discord）、`schedules/`（cron 定时任务）、`subagents/` 和 `agent.ts`（模型与运行时配置）。
- **工具系统**：通过 `defineTool` 用 Zod Schema 声明工具，自动提供类型安全的执行环境。
- **技能与子代理**：支持按需加载的 Markdown 过程（skills）和嵌套子代理（subagents），适合复杂工作流。
- **多渠道接入**：原生支持 HTTP、Slack、Discord 等通道，可一键接入消息服务。
- **评估与清理**：`eve eval` 可本地运行一次性评估，并在退出时清理沙箱计算资源。
- **完整文档内置**：npm 包中包含全部文档，方便编写代理的 AI 助手直接读取 `node_modules/eve/docs`。

## 适用场景

- 需要长期维护、多人协作的 AI 代理（文件结构天然适合版本控制）。
- 内部工具自动化，如定时周报生成、Slack 机器人、客服应答。
- 原型快速验证：通过 `init` 一条命令即可搭建可交互的代理。
- 对安全有要求的评估环境（沙箱隔离）。

## 同类对比

- **vs LangChain**：LangChain 以代码为中心，eve 以文件约定为中心，结构更清晰，但灵活性不如 LangChain 的链式抽象。
- **vs CrewAI**：CrewAI 侧重多智能体协作，eve 当前更偏向单代理的模块化，子代理功能可作为扩展。
- **vs Vercel 自家 AI SDK**：AI SDK 更底层，提供模型统一接口；eve 在其上封装了代理生命周期、工具、调度等全栈功能。

## 版本动态

- 当前版本 `eve@0.21.1`（2026-07-07）。
- 最近修复：`eve eval` 在运行后能清理本地沙箱句柄，防止 eval 进程结束后资源残留。
- 项目处于 Beta 阶段，API 与行为可能随 GA 变化，但更新频率和问题响应积极。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未说明具体支持的全部模型提供商（示例仅出现 Anthropic）；未提供沙箱（microsandbox）的实现细节与隔离级别；无性能基准或资源占用数据；未明确生产环境部署方式（如是否强依赖 Vercel 平台）；Node.js 最低版本要求缺失