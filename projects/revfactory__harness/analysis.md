## 它是什么
Harness 是一个 Claude Code 的**团队架构工厂**，位于生态的 L3 Meta-Factory 层。用户只需输入领域描述（如“构建一个用于深度研究的 harness”），它会自动分析需求、选择 6 种预定义团队模式之一，并生成 `.claude/agents/` 和 `.claude/skills/` 目录下的 Agent 定义与技能文件。整个过程由 6 阶段工作流驱动：领域分析→架构设计→Agent 定义→技能生成→集成编排→验证测试。

## 为什么火
项目在 2026 年 3 月发布后迅速积累 7500+ Star，因为它直击 LLM 多 Agent 编排的痛点——手动拆分任务、定义 Agent 角色和传递规则非常耗时。Harness 将团队设计模式化、自动化，且提供了可复用的团队架构（Pipeline、Fan-out/Fan-in、Expert Pool、Producer-Reviewer、Supervisor、Hierarchical Delegation）。其配套的 A/B 测试显示，使用 Harness 后代码质量平均提升 60%（49.5→79.3），15 项任务全胜，产出方差下降 32%。

## 技术栈
- 载体：纯 Markdown 配置文件（AGENTS.md、SKILL.md），无额外代码运行时依赖
- 分发：Claude Code Plugin 系统（支持 marketplace 安装），也支持直接复制 skill 目录
- 架构模式：内建 6 种可组合的团队组织模式，以提示词和编排模板实现
- 生成策略：渐进式披露（Progressive Disclosure），按上下文按需加载技能细节，优化 token 消耗

## 核心能力
- **模式化团队生成**：6 种架构覆盖串行、并行、专家池、生产-审查、监督、层级委托等场景
- **技能自动生成**：遵循渐进式披露，生成多级技能文件，保持 Agent 上下文高效
- **编排与验证**：内置错误处理、数据传递协议，支持触发验证、干运行测试、有/无技能对比评估
- **多语言触达**：支持韩文、日文触发词，国际化演示
- **生态配套**：衍生仓库 `harness-100` 提供 100 个开箱即用的团队配置，覆盖 10 个领域

## 适用场景
- 内容创作：如 Webtoon 剧集制作、YouTube 内容规划
- 软件工程：代码审查、重构、全栈网站开发
- 数据与 AI：数据管道设计、LLM 应用开发
- 研究与文档：深度调研、API 文档生成
- 营销与策略：营销活动策划、商业分析

## 同类对比
| 工具 | 定位 | 与 Harness 关系 |
|------|------|-----------------|
| Archon | 确定性运行时配置工厂 | 同一层（L3），不同子层：Archon 管运行时 reproducible，Harness 管团队架构设计 |
| meta-harness | 同一概念的 Codex 运行时移植 | 不同运行时：Claude Code vs Codex，互补 |
| ECC (everything-claude-code) | 跨 harness 的标准化层（L2） | 上层消费者：ECC 可叠加在 Harness 生成的 harness 上 |
| wshobson/agents | 子 Agent/技能目录（182 Agent, 149 Skill） | 零件库：Harness 可引用目录中的部件组装团队 |
| LangGraph | 状态图编排，LLM 无关 | 不同赛道：LangGraph 面向长运行、状态恢复，Harness 面向 Claude Code 原生快速搭建 |

## 版本动态
- 最近推送：2026-06-10
- 当前版本：1.2.0
- 创建于 2026-03-26，Star 数增长快，目前 7543
- 已进行首次 A/B 测试研究，数据较正面（自测），第三方复现尚在计划中
- 配套仓库 `harness-100` 已发布 1808 个 Markdown 文件，涵盖 10 个领域
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：A/B 测试为作者自测，第三方复现尚未完成；README 未明确说明所需 Claude Code 最低版本；直接安装方式仅限于 skill 文件，未说明是否需要额外配置插件注册；语言标签误标为 HTML，实际为 Markdown 配置