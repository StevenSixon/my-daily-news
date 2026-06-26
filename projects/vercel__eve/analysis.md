## 它是什么

eve 是 Vercel 推出的 agent 框架，采用文件系统优先的设计，将代理的能力（指令、工具、技能、通道、调度）约定为固定目录和文件。项目结构即配置，使得 AI 代理可读、易维护。

## 为什么火

Star 数快速增长（2661），源于 Vercel 的品牌效应和开发者对可组合代理的渴求。文件系统布局降低了认知负担，结合 Markdown 指令和 TypeScript 工具定义，让构建生产级 agent 像写传统应用一样自然。

## 技术栈

- 核心语言 TypeScript，运行于 Node.js  
- 通过 npm 包 `eve` 提供脚手架、运行时和类型  
- 模型对接多种 LLM（示例用 claude-sonnet-4.6），通过 `agent.ts` 配置  
- 兼容 Vercel 部署，支持 Docker/microsandbox 本地后端，部署时需切换兼容后端  
- 工具定义使用 Zod 进行输入校验  

## 核心能力

- **文件系统即接口**：`agent/` 目录下规范放置 instructions.md、tools/、skills/、channels/、schedules/  
- **持久化代理**：框架自称 “durable”，暗示支持状态保持和长运行  
- **多通道支持**：内置 Slack、HTTP 等消息通道  
- **人机协同**：可添加 human-in-the-loop 提示  
- **子代理与技能**：按需加载的 Markdown 过程文件  
- **评估辅助**：提供 `mockModel` 评估工具  
- **调度任务**：cron 表达的定时工作  

## 适用场景

- 需要快速搭建含工具、多通道的交互式 AI 助手  
- 希望在项目中保持代理逻辑与业务代码相邻，便于团队协作  
- 构建内部工具、Slack 机器人、定期报告 agent  

## 同类对比

相比于 LangChain 的代码为中心、AutoGPT 的自治模式，eve 更强调约定优于配置，适合希望减少抽象层的 TypeScript 开发者。与 Vercel AI SDK 互补，但 eve 更聚焦 agent 结构化和全生命周期管理。目前仍 beta，文档和稳定性和成熟度不如 LangChain。

## 版本动态

最新 0.15.4（2026-06-26）修复了 Slack 状态文本的 Markdown 剥离、新增 mockModel 评估工具、为多 agent 部署隔离工作流队列前缀，以及优化 Vercel 构建失败提示。迭代活跃，功能扩展迅速。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未说明支持的 Node.js 最低版本；未提供性能基准或与同类框架的对比；未列出完整支持的 LLM 提供商/模型列表；持久化机制细节未在 README 中展开；与 Vercel AI SDK 的协作关系未明确说明