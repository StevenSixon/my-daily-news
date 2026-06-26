## 它是什么
Agent-Native 是 BuilderIO 开源的 Agent 应用框架，核心理念是让 Agent 作为应用的“一等公民”，直接操控 UI、状态和数据，而非仅以聊天窗口外挂。提供 actions、agent runtime、SQL 状态管理、多协议端点（HTTP/MCP/A2A/CLI）等全套基元。

## 为什么火
- 解决 Agent 与产品UI割裂的问题：传统 AI 只能通过聊天窗口交互，Agent-Native 让 Agent 所见即所得，操作与用户点击共用同一 action 定义。
- 开箱即用的模板（邮件、看板、文档等）可直接克隆，降低启动成本。
- 后端无关（任意兼容 Drizzle 的 SQL 库，Nitro 托管），用户掌控代码和部署。

## 技术栈
- 语言：TypeScript
- 核心库：@agent-native/core, @agent-native/skills
- 状态：SQL 数据库（需 Drizzle 适配器）
- 部署：任意支持 Nitro 的平台
- 协议：HTTP, MCP, A2A (Agent-to-Agent), CLI

## 核心能力
- **Actions 复用**：一次定义，UI 点击、Agent 调用、API、MCP、CLI 等端通用。
- **Agent 运行时**：内置对话、工具调用、技能、记忆、定时任务、可观察性、转交（handoffs）。
- **实时协作**：人和 Agent 共享同一数据库，状态实时同步。
- **上下文感知**：Agent 知道用户当前聚焦的界面元素，可选中文本按 Cmd+I 指示操作。
- **Agent 间调用**：通过 A2A 协议跨应用协调。
- **自我演化**：Agent 可添加功能、修 bug、优化 UI。

## 适用场景
- 构建下一代 AI 原生 SaaS（如邮件、日历、文档编辑工具），Agent 深度参与交互和功能修改。
- 需要 Agent 与真实应用界面协同操作的内部工具或原型。
- 快速搭建可定制、自托管的 Agent 前端应用，如视觉规划工具、内容编辑器等。

## 同类对比
- 相比纯 Agent 框架（如 LangChain、AutoGPT）：Agent-Native 更强调与 UI 的共生，提供完整的前端接入，而不仅是逻辑编排。
- 相比传统 SaaS 工具：用户拥有代码，可完全自定义，Agent 能动态改应用。
- 相比 copilot 式聊天助手：不再外挂聊天窗口，Agent 在应用内直接行动，多模态交互。

## 版本动态
- 2026-03 创建，活跃开发中，最新 Release 为 @agent-native/skills@0.2.140 (2026-06-26)。
- 核心库 @agent-native/core@0.79.12 频繁迭代。
- 文档初步完善，包含 auth、neon-netlify 集成等指南。
---

## ℹ️ 置信度与信息盲区

- 置信度：**medium**
- 信息盲区：许可协议信息矛盾：README 声明 MIT，但仓库元数据显示 None；无性能基准或压力测试数据；未明确 Auth 实现细节及第三方认证支持范围；未说明生产环境部署建议和高可用方案；缺少 actions/runtime 的详细 API 文档链接（未提供全文）