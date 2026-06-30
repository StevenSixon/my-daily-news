## 它是什么
Loop Engineering 是一套面向 AI 编码代理（如 Grok、Claude Code）的**设计系统**，提供可复用的循环模式、脚手架和 CLI 工具。它停止“手写提示”，转而设计一个持续运行的循环来自动发现、分派、实施和验证任务，并给出**就绪度评分**。

## 为什么火
Addy Osmani 和 Anthropic 的 Boris Cherny 等一线技术领袖公开推崇类似理念，项目在短时间内获得 4.3k Star。其“设计循环而非编写提示”的范式转变切中了当前 AI 编码代理从实验走向生产的关键痛点：**可重复性、成本控制和安全审计**。

## 技术栈
- 核心语言：JavaScript / Node.js
- 发包：多个 NPM 包（@cobusgreyling/loop-*），支持 npx 直接使用
- 集成示例：Grok, Claude Code, Codex, OpenClaw, GitHub Actions
- 文档：Jekyll + GitHub Pages 交互式展示
- 测试与 CI：自带 `loop-audit` 工作流 dogfooding

## 核心能力
1. **模式库**：7 种经过验证的生产循环（每日分诊、PR 保姆、CI 清理等），含成本和风险等级
2. **审计工具**：`loop-audit` 对项目进行打分，检查 LOOP.md、STATE.md、约束文件等，输出就绪度（0-100）和提升建议
3. **成本估算**：`loop-cost` 根据模式和频率估算令牌消耗
4. **漂移检测**：`loop-sync` 检查配置文件间的一致性，防止配置腐烂
5. **约束执行**：`loop-constraints` 提供结构化护栏文件和技能，防止代理越权操作
6. **MCP 服务**：为外部系统提供模式、技能和状态的查询接口

## 适用场景
- 已有 AI 编码代理（Grok、Claude Code 等）并希望**安全地自动化重复开发任务**的团队
- 希望通过**可审计、可评分**的方式逐步将代理升级到无人值守模式的工程经理
- 需要评估**代理运营成本**和**就绪度**的技术决策者

## 同类对比
- 与直接使用 GitHub Actions 或 cron 脚本调度代理相比，Loop Engineering 提供了完整的设计语言、就绪度评分和渐进的 L1-L3 安全发布路径
- 与 LangChain 等代理框架不同，该项目不绑定特定模型调用，而专注于**操作层面的编排和治理**
- 缺失：未提供代理运行时，需要自行集成具体代理的 CLI 或 API

## 版本动态
v1.5.0 是近期大版本，合并了 7 个社区 PR，新增 `loop-sync`、`loop-constraints` 和 `loop-mcp-server`，完善了配置漂移检测和护栏体系，显得社区活跃且迭代迅速。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未明确执行代理时需配置的具体 API 密钥或服务端点；token 成本估算模型的准确性未提供基准数据；loop-mcp-server 的 npm 包尚未发布，仅有源码