## 它是什么
eve 是 Vercel 推出的文件系统优先的 AI Agent 框架，使用 TypeScript。通过 agent/agent.ts、instructions.md、tools/、skills/、channels/、schedules/ 等约定目录来组织 Agent 的全部能力，强调项目可审查与可扩展，避免黑盒式 Agent 实现。

## 为什么火
Vercel 的品牌加持加上对 Agent 工程化痛点的针对性解决（约定优于配置），使它在发布短时间内获得 2831 Star。社区活跃于 GitHub Discussions，但项目尚处 beta，API 可能变动。

## 技术栈
TypeScript + Node.js，定义工具使用 defineTool + Zod schema，模型配置通过 defineAgent 指定（如 anthropic/claude-sonnet-4.6）。内置 channels（HTTP/Slack/Discord）、schedules（cron），底层可能依赖 Vercel Workflows 基础设施。文档集成在 npm 包内，方便本地 AI 编码工具查阅。

## 核心能力
- **文件系统即创作界面**：无需重型 IDE 集成，目录结构就是 Agent 蓝图。
- **工具与技能分离**：工具是模型可直接调用的函数，技能是按需加载的过程。
- **多通道接入**：原生支持 Slack、Discord 等消息通道。
- **定时任务**：通过 schedules 定义 cron 作业。
- **本地开发体验**：一条命令 `npx eve@latest init` 创建项目，`npm run dev` 启动交互终端 UI。

## 适用场景
需要快速构建可维护 AI Agent 的 TypeScript 团队，尤其适合：
- 内部流程自动化（如定时总结、周报生成）
- 聊天机器人（Slack/Discord 集成）
- 工具调用型 Agent（天气查询、数据检索）
- 已在 Vercel 生态中的项目

## 同类对比
与 LangChain（重抽象、生态大）相比，eve 更轻量、更约定化；与 AutoGPT 等独立 Agent 相比，更侧重工程化与可审查性。但目前生态较小，且与 Vercel 平台绑定较深。

## 版本动态
当前 beta 版本 eve@0.16.2（2026-06-27），最近的 patch 禁用了 Workflow SDK turbo 第一交付路径，回归全序运行时路径。这表明框架仍在快速调整执行引擎，生产使用需关注变更。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未明确部署到生产是否需要 Vercel 账户或特定定价计划；未提供性能或可靠性 benchmark 数据；subagents 和 schedules 的具体实现限制与持久化机制未在 README 展现；与 Vercel Workflows 的依赖关系及独立部署可行性未说明