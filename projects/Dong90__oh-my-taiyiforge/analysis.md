## 它是什么
TaiyiForge（太一炉）是一个 AI 研发工作流自动化插件，将传统的软件工程标准编排成一条可执行、可审计的**九阶段流水线**。它不发明新标准，而是把 Harness、OpenSpec、GStack、Superpowers、OMO、Spec-Kit 等六个现有规范的流程变成一台状态机，通过统一的 slash 命令在 Claude、Codex、Cursor、OpenCode 四类 AI 终端中提供一致行为。开发者只需要说 `/taiyi:new`，引擎就会生成对应的工件、校验门控并自动推进阶段。

## 为什么火（关注点）
- **流程断裂是 AI 编码的普遍痛点**：长会话中 Agent 容易忘掉阶段顺序，导致需求丢失或设计半成品直接跳入编码，TaiyiForge 用状态机强制阶段顺序和工件产出，避免了“玄学”式开发。
- **多工具统一**：不同 AI 终端（Claude Code、Codex、Cursor、OpenCode）各自一套流程，团队难以复用。TaiyiForge 提供一套 28 条 v28 顶栏命令，在任何终端行为一致，降低认知负荷。
- **人类门控与自动化的平衡**：关键节点（变更审批、设计评审）要求 `--approver` 人类确认，避免了完全自动化的风险；小修复也有 `flow bug` 快捷路径，不死板。

## 技术栈
- 语言：TypeScript
- 包管理：npm，零构建安装（npx 分发）
- 运行环境：Node.js >= 20
- 集成方式：通过 shell 脚本、MCP、命令文件注入 AI 终端的命令系统
- 工程化：GitHub Actions CI，829 测试用例，130 源文件

## 核心能力
- **九阶段主流程**：change → requirement → design → ui-design → task → dev → test → review → integration → archive，每阶段有固定产出工件（如 CHANGE.md、DESIGN.md）和自动门控校验。
- **v28 统一命令**：28 条顶栏 slash 命令，分为主链、会话、排查、交付、路由、捷径、伞形命令（Umbrella）七组，覆盖日常开发全流程。
- **多终端适配**：一键安装到 Claude Code、Codex、Cursor、OpenCode，缺端自动跳过；在 Codex 中自动转换为关键词路由。
- **聊天与引擎分轨**：用户用 slash 命令，Agent/CI 用 CLI（`npx taiyi`）运行门控校验和流程推进，避免将大量工件塞入聊天引起上下文爆炸。
- **Skill 系统**：内置 `taiyi-*` Skill，如 `taiyi-dev` 强制 TDD（先红后绿），`taiyi-review` 支持跨 AI 评审。
- **人类审查+自动审计**：关键阶段强制人类批准，集成 `taiyi_doctor`、`taiyi_audit` 自检与交付门控。

## 适用场景
- 使用 AI 编程助手进行严肃软件开发的团队（尤其多 AI 工具混合使用）
- 需要结构化、可审计、可复用的 AI 驱动研发流程
- 多人协作、跨会话、持续交付的项目
- 不想背诵复杂流程，希望“引擎告诉我下一步”的开发者

## 同类对比
- 相较于直接使用 OpenSpec、Harness 等原始规范：TaiyiForge 将其组合成可编排的状态机，减少了人工串联步骤。
- 相较于各 AI 终端原生的 agent 模式：提供了统一的工件锁定和阶段门控，避免了 Agent 忘掉流程。
- 相较于单一工具的内置流程（如 Cursor Rules）：跨工具一致性更好，且支持人类审查标记。

## 版本动态
- 最新 Release：v0.38.0 (2026-06-22)，合并 20 个 PR，文档同步，质量审计满分，829 个测试通过。
- 近期发展：v0.24 引入零构建安装，v0.25 支持 GitHub 直装，v28 命令体系稳定。
- 活跃迹象：快速迭代，命令收敛、安装流程简化。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：六套集成标准各自的深度和兼容边界未详细说明；无性能基准或大规模团队的使用数据；与 IDE 插件的具体交互细节（如 Cursor 规则文件的格式）仅部分覆盖；README 截断，可能遗漏后续的架构细节和 API 文档