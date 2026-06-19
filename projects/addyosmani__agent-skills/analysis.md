## 它是什么

Agent Skills 是一套面向 AI 编码代理的生产级工程技能包，由 Google Chrome 开发者关系负责人 Addy Osmani 维护。它把资深工程师在软件开发全生命周期中使用的工作流、质量关卡和最佳实践打包成 24 个结构化技能，通过 7 个斜杠命令（`/spec`、`/plan`、`/build`、`/test`、`/review`、`/code-simplify`、`/ship`）自动激活，覆盖从想法精炼到生产交付的每个环节。技能以 Markdown 编写，与任何能读取系统提示或指令文件的 AI 代理兼容，内置反模式表、验证步骤和安全边界。

## 为什么火

项目在短时间内获得 63k+ Star，成为 AI 辅助开发领域的热点。核心原因：1）填补了 AI 代理“会写代码但不懂工程纪律”的空白——代理往往能生成正确代码，却忽略测试策略、安全审查、性能约束等工程上下文；2）标准化程度高，一套技能可跨 Claude Code、Cursor、Copilot、Gemini CLI、Antigravity 等工具复用；3）由 Addy Osmani 和众多贡献者持续打磨，引入威胁建模、可观测性、浏览器性能审计等现代工程主题；4）社区驱动，PR 活跃，快速适配新 IDE 和 CLI，且许可证宽松（MIT）。

## 技术栈

- **技能格式**：Markdown + 结构化工作流指令，利用原生 AI 系统的 prompt/rule 机制。
- **支持平台**：Claude Code（官方插件市场）、Antigravity CLI（原生插件）、Cursor（`.cursor/rules/`）、GitHub Copilot（`agents/` 代理定义）、Gemini CLI、Windsurf、OpenCode、Kiro 以及任意可注入指令的工具。
- **关键依赖**：自身不依赖特定运行时，仅用 Markdown。在浏览器测试技能中使用 Chrome DevTools MCP 协议进行运行时交互；可观测性技能引入 OpenTelemetry 等最佳实践。
- **自动化**：通过 `/build auto` 一键生成计划并全自动实施，保留按任务独立提交和测试验证。

## 核心能力

- **全生命周期命令**：`/spec`（定义需求）→ `/plan`（拆解任务）→ `/build`（增量实现）→ `/test`（验证）→ `/review`（质量审查）→ `/code-simplify`（简化代码）→ `/ship`（交付上线）。
- **24 项技能**：涵盖元技能（路由到正确工作流）、用户访谈（`interview-me`）、想法精炼、规范驱动开发、任务拆解、增量实现、TDD、上下文工程、源码驱动开发、怀疑驱动开发、前端工程、API 设计、浏览器 DevTools 测试、调试与纠错、代码审查与质量、代码简化、安全加固、性能优化、Git 工作流、CI/CD、弃用与迁移、文档与 ADR、可观测性、发布上线。
- **代理角色**：预配置的代码审查员、测试工程师、安全审计员、性能审计员等 specialist 角色，直接调用。
- **安全增强**：最新版加入威胁建模、SSRF 防护、供应链及 AI/LLM 专项安全技能。
- **可观测性**：RED 指标、结构化日志、分布式追踪、基于症状的告警模式。

## 适用场景

- 使用 AI 编码工具的个人开发者或团队，希望强制代理遵守 TDD、代码审查、安全扫描等工程纪律。
- 从零到一的绿场项目，用 `/spec` → `/build auto` 快速产出一致、可验的代码基。
- 棕场遗留系统改造：通过安全加固、性能优化、代码简化等技能进行系统化治理。
- 跨工具协同：同一套技能在 Claude Code 和 Cursor 等不同 IDE 间保持一致，降低团队认知成本。
- 教育与 onboarding：新成员通过技能指令学习资深工程师的决策习惯和质量标准。

## 同类对比

- **与 cursor-rules、copilot-instructions 等相比**：多数项目仅提供散装 best-practice 提示词或特定语言模板，Agent Skills 是一套正交于语言/框架的工程方法论，有清晰的生命周期映射和反模式防御。
- **与 DevQualityGPT 等质量工具相比**：更偏重于代理执行过程中的即时约束，而非事后检查。
- **与 OpenHands、Aider 等编码代理自带指令相比**：Agent Skills 强调可移植，不会被绑定在单一平台，且覆盖从需求到部署的全过程，更为系统化。
- **独特点**：引入“怀疑驱动开发”、源码驱动开发、上下文工程等元技能，将软件设计层面的思维模式代码化，这是绝大多数技能库所不具备的。

## 版本动态

- 当前版本 **0.6.2**（2026-06-11），上一版本 0.6.1。
- 本次更新重点：修复市场安装中 SSH/HTTPS 问题；将安全技能从普通 checklist 扩展为包含威胁建模、SSRF、供应链及 AI/LLM 攻击面的深度技能；新增 `web-performance-auditor` 代理和 `/webperf` 命令；新增 `observability-and-instrumentation` 技能；新增 Antigravity CLI 原生支持（`agy plugin install`）。
- 社区贡献者活跃，多个 PR 涉及文档修正、新功能添加和集成适配，发布节奏稳定，可见项目仍处于快速发展期。