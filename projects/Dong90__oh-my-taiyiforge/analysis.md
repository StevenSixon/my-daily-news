## 它是什么
TaiyiForge（太一炉）是一套把 AI 代码生成过程强制编排为九阶段流水线的工具。通过状态机引擎，约束 Claude、Codex、Cursor 等 AI 终端必须按序产出需求、设计、任务拆分、TDD 开发、测试证据和人工审批，避免 Agent “偷跑”。

## 为什么火
当前 AI 辅助编程普遍存在流程跳跃、上下文丢失、多工具行为不一致的痛点。TaiyiForge 用 Skill 插件统一指令集，用硬门控阻断跳过设计，用 token 压缩机制保持长会话可持续，击中工程团队对 AI 产出的审计需求。其 `/taiyi:plan` 一键生成全栈骨架的 auto 模式（79 文件，1,170 测试 0 失败）展示了直接可用的工程化产出能力。

## 技术栈
- 语言：TypeScript
- 分发方式：npm 包，通过 `npx taiyi-forge-install` 安装 Skill 到各 AI 终端（Claude Code、Cursor、OpenCode、Codex）
- 测试：151 个测试文件，1,170 测试用例，包含 CLI 冒烟测试、Agent 角色测试、E2E
- 许可证：MIT

## 核心能力
- **九阶段契约流水线**：change → requirement → design → ui-design → task → dev → test → review → integration，每阶段固定产出，关键节点人工审批。
- **跨终端统一指令**：28 条规范 slash 命令，同一套词汇在各平台行为一致。
- **项目级规划**：`/taiyi:plan` 接收 README/PRD/PDF/URL，自动分解为独立变更模块，支持半自动确认或全自动生成骨架（含 FastAPI 后端、前端、测试、Docker 等）。
- **强制 TDD + evidence**：dev 阶段先红后绿，每个验收标准必须有可执行验证命令，打通过门控。
- **上下文管理**：长会话自动产出上下文压缩文档，支持跨天续接。
- **柔性 profile**：提供 full、lite、nano 等 8 种流程裁切，适应不同规模需求。

## 适用场景
- 用多个 AI 编程工具、但希望流程标准化的团队
- 需要产出可审计设计文档和测试证据的项目
- 想从零快速生成全栈项目骨架（FastAPI 后端 + 前端）的场景
- 已有 Harness、OpenSpec、Superpowers 等插件的用户（TaiyiForge 将其编排成统一状态机）

## 同类对比
与直接和 AI 对话比，TaiyiForge 用状态机保证阶段不跳、审批硬拦、上下文持久化。相比 oh-my-claudecode / oh-my-codex 等单一工具插件，它实现了跨终端一致性和项目级规划能力，但不提供 AI 模型本身，定位为流程编排壳。

## 版本动态
v1.0.0（2026-06-28）为首个正式版，包含 609 个文件、2.8 万行代码变更、8 套完整示例工程。仓库创建仅 23 天即发布稳定版，迭代速度极快。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未明确最小 Node.js 版本要求；无性能基准测试数据；与其他工作流工具（如 Aider、Continue）的具体对比缺失；未说明是否支持非 FastAPI 技术栈生成