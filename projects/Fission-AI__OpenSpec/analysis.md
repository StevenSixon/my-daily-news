## 它是什么

OpenSpec 是一个面向 AI 编码助手的规范驱动开发（Spec-Driven Development）框架。它要求在写代码之前，人类和 AI 先通过对齐规范达成共识，将需求、设计、任务以结构化目录（proposal.md、specs/、design.md、tasks.md）落盘，避免需求仅存在于聊天历史中导致的不可预测性。

## 为什么火

- 创建于 2025-08，不到一年获 57k+ Star，反映出 AI 编码助手普及后，开发者对结构化工作流的强烈需求。
- 口号“fluid not rigid, iterative not waterfall”击中 AI 辅助开发中“灵活与规范失衡”的痛点。
- 支持 Cursor、Claude Code 等 25+ 工具，不需锁定特定 IDE 或模型。

## 技术栈

- CLI 工具：TypeScript/Node.js（≥20.19），通过 npm 分发。
- 与 AI 工具集成：通过斜杠命令（/opsx:explore、/opsx:propose、/opsx:apply、/opsx:archive 等）在 AI 对话中直接使用。
- 文件系统驱动：所有规范存储在项目 openspec/ 目录中，兼容任意版本控制系统。

## 核心能力

- **探索模式（/opsx:explore）**：无压力头脑风暴，AI 先阅读代码再给方案，不生成任何文件。
- **提议（/opsx:propose）**：生成完整的变更目录，包含提案、规格、设计、任务清单。
- **应用（/opsx:apply）**：按 tasks.md 逐项实现。
- **归档（/opsx:archive）**：完成后将变更移至 archive，更新主规格。
- **灵活迭代**：无严格阶段门控，任何产物可随时编辑，适应当今 AI 协作的快节奏。
- **多 profile 支持**：默认 profile 提供核心命令；可选扩展 profile（/opsx:new、/opsx:continue、/opsx:ff、/opsx:verify 等）可按需启用。
- **团队协作（Stores Beta）**：支持将规范分离到独立仓库供团队共享。

## 适用场景

- 用 AI 编码助手（Cursor、Claude Code、Copilot 等）做严肃开发的个人或团队。
- 特别适合存量项目（brownfield）的增量迭代，OpenSpec 设计上优先考虑对现有代码库的适配。
- 从个人项目到企业级均可伸缩。

## 同类对比

- **vs GitHub Spec Kit**：Spec Kit 更重量级，有严格阶段门控，大量 Markdown 模板，依赖 Python。OpenSpec 更轻便、灵活，强调“流体”工作流。
- **vs AWS Kiro**：Kiro 功能强大但锁定其 IDE 和 Claude 模型。OpenSpec 工具和模型无关，适用于已有工具链。
- **vs 无规范**：直接裸用 AI 易导致需求漂移和不可预期输出，OpenSpec 以最小仪式感引入可预测性。

## 版本动态

- 当前最新 Release：v1.4.1（2026-06-03），修复了 `openspec update` 在含自定义 workspace.yaml 项目中的兼容问题。
- README 已推荐新的 artifact-guided 工作流（/opsx:propose → /opsx:apply → /opsx:archive），并暗示旧的命令工作流可能被简化或逐步替代。
- 社区 Schema 机制正在发展，类似 Spec Kit 的扩展目录，允许第三方提供集成工作流。
- 维护者推荐高推理模型（Codex 5.5、Opus 4.7）以获最佳效果。

---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：多语言支持的具体语言列表未在 README 列出；无性能基准或大规模项目量化收益数据；Stores 功能尚处 Beta 阶段，稳定性和极限未说明