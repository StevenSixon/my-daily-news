## 它是什么

eve 是 Vercel 发布的一份文件系统优先的 AI Agent 框架。它把 Agent 的核心能力（指令、工具、技能、通道、定时任务）映射到约定目录，开发者通过编辑 Markdown 和 TypeScript 文件来定义 Agent 的行为，项目天然可读、可版本化。运行时基于 Node.js，支持模型配置、多通道（Slack/Discord/HTTP）和沙箱执行。

## 为什么火

虽然刚刚发布，但 Vercel 的品牌吸引力、文件约定的简洁理念，以及内置的多通道支持和沙箱，让它迅速获得关注。相比过度抽象的框架，它更贴近“代码即配置”的极客口味，降低了 Agent 项目的入门和维护门槛。

## 技术栈

- 语言：TypeScript
- 运行时：Node.js
- 模型接入：通过 `model` 选项指定（如 anthropic/claude-sonnet-4.6），依赖 Vercel 的模型网关或直接调用
- 工具定义：使用 Zod 进行参数校验
- 沙箱：微沙箱（microsandbox）用于隔离执行
- 通道：内置 Slack、Discord、HTTP 等通道支持
- 文档内建：`node_modules/eve/docs` 包含完整文档

## 核心能力

- **指令优先**：`instructions.md` 作为永久系统提示
- **工具函数**：`tools/` 下定义可调用函数，类型安全
- **技能**：`skills/` 中按需加载的 Markdown 过程
- **通道**：`channels/` 支持多平台消息接入
- **定时任务**：`schedules/` 中用 cron 表达式触发
- **人工介入**：支持 human-in-the-loop 提示
- **子代理**：`subagents/` 实现代理协作
- **评估**：内置 evals 目录用于测试与评估
- **沙箱执行**：隔离运行工具和技能，避免副作用

## 适用场景

- 需要长期运行的持久化 Agent，如团队助手、定时报告机器人
- 多渠道交互的智能助手（Slack + Discord + HTTP）
- 需要复杂工具链和子代理编排的自动化流程
- 偏好文件约定和 Git 工作流的团队

## 同类对比

对比 LangChain / CrewAI 等框架，eve 的核心差异是“文件系统即接口”而非复杂的编程抽象。它更像 Next.js 之于 React 的定位——通过约定减少决策成本。与 Vercel AI SDK 可能互补：SDK 面向 API 调用，eve 面向完整 Agent 工程。因尚处 beta，生态和社区扩展性不如老牌框架。

## 版本动态

最新 0.11.7（2026-06-19）包含多项改进：沙箱创建进度上报、引擎安装序列化避免 race condition、Slack 打字指示器分段更新等。项目迭代活跃，Commit 记录密集，说明核心团队在快速打磨体验。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供性能 benchmark 数据；生产部署是否需要 Vercel 账户或可完全自托管未明确；微沙箱的安全边界与实现细节未深入说明；与 Vercel AI SDK 的具体整合路径未展开