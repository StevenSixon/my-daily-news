## 它是什么
ECC（Agent Harness Operating System）是一个面向 AI 编程助手（Claude Code、Codex、OpenCode、Cursor、Gemini、Zed 等）的**跨 harness 运行时系统**。它提供的不是简单的配置文件集合，而是一整套生产级的技能库、记忆持久化、安全扫描、持续学习与多 agent 编排框架。目前已演进至 v2.0.0，包含 261 个公开技能、64 个 agent 定义和 84 个命令。

## 为什么火
1. **跨 harness 统一抽象**——通过 `ecc.session.v1` 适配器协议，屏蔽不同工具间的差异，同一套 skills/rules/hooks 可在 Claude Code、Cursor、Codex 等之间复用，避免多工具割裂。
2. **生产级可观测性**——自带的 control-pane 提供会话指标、工作项看板、MCP 库存漂移检测，甚至曾在开发阶段抓出一次真实的 secret 泄露。
3. **开箱即用的编排能力**——`orch-*` 技能族支持多 agent fan-out、worktree 生命周期管理、合并冲突预测，适合大规模 parallel agent 协作场景。
4. **社区与商业双轨**——220K+ star、230+ 贡献者，MCP 生态集成积极，同时提供 Pro 版（$19/月/席位）用于私有仓库。

## 技术栈
- 主体为 JavaScript/TypeScript 实现
- 控制面板：Rust 编写的原型（`ecc2/` 目录，处于 alpha 状态）
- 提供 npm 包：`ecc-universal`、`ecc-agentshield`
- 支持 Shell、Python、Go、Java、Perl、Markdown 等多语言生态
- 与 MCP（Model Context Protocol）深度绑定，提供 `ecc.mcp.v1` 库存统一视图

## 核心能力
- **261 个公开技能**：覆盖编码、研究、安全、媒体、企业运维、agent 工作流
- **Session 适配器**：统一的多 harness 会话 schema，追踪“哪个 agent 在哪、做什么”
- **MCP 库存管理**：跨 harness 归一化视图、配置漂移检测、secret 自动脱敏
- **Worktree 生命周期服务**：并行 agent 工作树的合并冲突预测与安全 GC
- **编排能力**：`orch-*` 技能族支持动态多 agent 分工与 fan-out
- **持续学习**：从会话中自动提取模式并沉淀为可复用技能（v2 规范已有）
- **AgentShield 安全扫描**：攻击面检测、沙箱化、敏感信息过滤
- **控制面板**（早期阶段）：本地 Web/TUI 面板展示会话指标、工作项看板、知识召回

## 适用场景
- 同时使用多个 AI 编程工具并希望统一配置与工作流的重度用户
- 需要多 agent 并行协作的复杂工程任务（大型重构、多服务联调）
- 将 AI 辅助开发纳入企业治理流程的团队（需要可观测、可审计的 agent 活动）
- MCP 生态的早期采用者，希望有一个统一的 MCP 服务器配置与监控平面

## 同类对比
- **vs 各 harness 原生配置**——ECC 将分散在 `.claude/`、`.cursor/`、`.codex/` 等目录的配置统一抽象，避免重复维护
- **vs 单独使用 MCP 服务器**——ECC 提供库存管理、漂移检测、secret 脱敏等生产化能力，而非仅仅连接
- **vs 自建 agent 编排方案**——ECC 的 `orch-*` 技能族和 worktree 管理提供了开箱即用的多 agent 协作模式
- 与 LangChain、AutoGPT 等 agent 框架并非直接竞争，更偏重 IDE/harness 层面的运行时整合

## 版本动态
- **v2.0.0 (2026-06-10)**：稳定版发布，261 技能、control-pane 底层、`orch-*` 编排族、Discord 社区上线
- **v2.0.0-rc.1 (2026-04)**：控制面板 GUI、operator 工作流扩展、优化技能包、预测市场工具（非投资建议）
- **v1.9.0 (2026-03)**：选择性安装架构、多语言扩展
- **v2.0.0 alpha**：Rust 控制平面原型已合入主干，提供 `dashboard`、`sessions`、`status` 等命令
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供性能 benchmark 数据（如技能加载耗时、跨 harness 切换延迟）；未展示 MCP 库存漂移检测的具体实现细节和误报率；v2.0.0 control-pane 的生产可用性未明确（标注为 early build）；未说明 261 个技能中多少已通过生产验证、多少为实验性；未列明支持的所有 MCP 服务器及兼容性矩阵