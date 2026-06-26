## 它是什么
Loop Engineering是一套针对AI编码代理（如Claude Code、Grok、Codex）的工程化实践，提供模式库、启动模板和三个CLI工具（loop-audit、loop-init、loop-cost），帮助开发者设计、审计和运行自主任务循环，替代手工逐条提示代理的方式。

## 为什么火
AI编码代理的普及使重复性任务（代码审查、依赖更新、Issue分类）自动化成为刚需，但直接写提示容易失控。该项目提供经过验证的模式与安全层级，让团队以“报告→辅助修复→无人值守”的渐进方式引入自动化，短期内star数快速攀升，反映了开发者对可操作代理编排的强烈需求。

## 技术栈
- 语言：JavaScript（Node.js）
- 工具链：npm包发布、GitHub Actions CI、monorepo结构
- 目标环境：支持Grok、Claude Code、Codex、GitHub Actions等
- 项目结构：patterns/（模式文档）、starters/（克隆即用模板）、tools/（三个CLI）、docs/（概念、安全、反模式等）

## 核心能力
- 7种生产级循环模式（日常分类、PR保姆、CI清扫、依赖清扫、变更日志起草、合并后清理、Issue分类），附带token成本估算与成熟度分级
- CLI工具套件：`loop-audit`（就绪度评分+徽章生成）、`loop-init`（脚手架生成项目循环配置）、`loop-cost`（花费预测）
- 五构建块+记忆模型：调度/自动化、工作树、技能、插件/MCP连接器、子代理，外加状态记忆
- 完整的运维指南：故障模式、反模式、多循环协调、运行与终止策略
- 安全与渐进式发布：L1（仅报告）→L2（辅助修复）→L3（自动合并），含allowlist/denylist机制

## 适用场景
- 团队中使用Claude Code、Grok、Codex等代理进行日常编码，希望将代码审查、CI失败修复、依赖升级等重复性工作自动化
- 需要可审计、可估算成本的代理任务编排，避免token爆炸
- 希望从单一提示工程转向系统化代理设计的开发者或技术负责人

## 同类对比
- 与GitHub Actions相比：Actions侧重CI/CD流水线，loop engineering专为AI代理的持续思维任务设计，提供状态记忆与验证闭环。
- 与LangChain/LlamaIndex等LLM框架相比：不解决模型调用，而是定义如何调度多个编码代理完成具体开发任务，更偏向运维与流程。
- 与单次提示技巧（如prompt engineering合集）相比：提供可复现、可度量、可进化的循环设计模式。

## 版本动态
- 项目创建于2026-06-09，截至2026-06-26保持活跃更新。
- 核心CLI版本：loop-audit v1.4（已加入活动检测）、loop-init v1.2、loop-cost具备基本功能。
- 自身dogfooding：通过GitHub Actions运行pattern验证与审计工作流，表明项目在持续自我验证。
- 社区推动：已接收adopters反馈，提供stories/目录分享真实案例。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供大规模生产环境的token消耗实测数据；未说明在非GitHub生态下的集成方案；CLI工具的具体覆盖率和误报率无量化指标；未展示多循环并发时的资源冲突处理细节