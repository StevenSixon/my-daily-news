## 它是什么
BuilderIO出品的Agent-Native框架，核心理念是让Agent成为应用的一等公民，而非附着在聊天界面的插件。通过统一的Action抽象，一次定义即可在UI组件、Agent工具、HTTP API、MCP工具、A2A接口及CLI中使用。Agent直接操作真实应用状态，与用户实时协作。

## 为什么火
2026年3月发布后短时间获3k+星，源于它提出了“Agent-Native”这一差异定位。传统AI应用在既有UI上叠加速成Agent，而Agent-Native在设计上让Agent与原生的UI、数据、逻辑共享同一套Action和数据库。提供邮件、日历、设计、分析等完整模板，降低了构建复杂Agent应用的门槛，且完全开源自托管，吸引了追求深度定制的开发者。

## 技术栈
- 语言：TypeScript
- 后端数据库：任何Drizzle兼容的SQL数据库
- 服务端运行环境：Nitro兼容宿主
- 前端框架：React（嵌入、交互及模板UI）
- 包管理：pnpm
- 协议支持：MCP、A2A、HTTP、WebSocket（推测用于实时协作）

## 核心能力
- **Action原语**：定义带有zod schema和run函数的Action，系统自动将该Action暴露为UI操作按钮、Agent工具、API端点、MCP工具、A2A接口和CLI命令，避免重复开发。
- **Agent运行时**：内置聊天、工具调用、技能、记忆、定时任务、可观测性及Agent间handoff，开箱即用。
- **双重身份UI**：Agent和用户平等操作同一UI，状态实时同步，支持选中文本→快捷键→Agent处理的内联交互，Agent之间可相互调用。
- **技能扩展**：可通过`npx @agent-native/core skills add`为现有编码Agent（Claude Code, Codex, Cursor等）增加可视化计划和回顾能力。
- **模板市场**：提供Clips（录屏+Agent排错）、Plans（可视化编码计划）、Design（设计原型）、Content（MDX编辑）、Slides（演示文稿）、Analytics（分析仪表板）等全栈模板，均可克隆并独立开发。
- **自托管与中立**：不锁定数据库或云平台，代码完全归开发者所有，支持任意数据库和部署方式。

## 适用场景
- 构建需要深度AI集成的SaaS产品：如协作工具、项目管理、内容创作、数据分析。
- 为现有编码助手增添可视化计划、代码审查等高级技能。
- 快速基于模板原型化Agent增强的应用，再逐步定制。
- 内部工具开发，让Agent参与业务流程操作而非仅回答问题。

## 同类对比
- **LangChain/LangGraph**：专注Agent工作流，无内置UI，需自己搭建应用壳。Agent-Native提供完整应用架构和UI-Agent对称的设计。
- **CopilotKit**：为React应用增加Copilot侧边栏，Agent与主应用松散耦合。Agent-Native让Agent直接操作应用状态，且Action可跨端复用。
- **Vercel AI SDK**：提供聊天和流式工具调用，但缺少统一的状态管理、多端Action暴露及应用级实时协作。Agent-Native更像Next.js之于React的定位——一个全栈框架。
- **Streamlit / Gradio**：偏数据展示而非Agent原生，且不提供统一的Action抽象跨端复用。

## 版本动态
最新版本`@agent-native/core@0.81.3`（2026-06-30）专注于修复MCP应用嵌入ChatGPT/Codex宿主的渲染问题：解决了空白iframe、尺寸不匹配、空嵌入显示等体验缺陷。显示团队正积极打磨与外部Agent宿主环境的集成稳定性。整体框架仍在0.x阶段，API可能变动，但已可投产使用。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供性能及规模基准数据；实时协作的底层技术（WebSocket/SSE等）未明确说明；认证模块具体支持的身份提供商和扩展细节未在README中展开（仅提及auth.md）；技能系统的完整开发指南和可扩展性未在片段中体现；0.x版本API稳定性及正式版路线图未披露