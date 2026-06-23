## 它是什么
LazyCodex 是 [oh-my-openagent (OmO)](https://github.com/code-yeongyu/oh-my-openagent) 的 Codex 适配发行版，将 OmO 的智能体调度、规划、执行与验证能力封装为一键安装的 Codex 插件，同时提供 Web 前端（Next.js + Tailwind v4）部署在 Cloudflare Workers。它类比 LazyVim 对 Neovim 的简化，让开发者无需深度配置即可在 Codex 中使用多智能体协作。

## 为什么火
OmO 本身社区热度极高（6 万星标），其质量检验严格，但因配置复杂让很多开发者望而却步。LazyCodex 通过 `npx lazycodex-ai install` 一条命令完成全部设置，并附带诊断命令，极大降低上手成本。同时它由 AI 助手 Jobdori 实时构建，与 OmO 版本同步，保证前沿特性快速落地。

## 技术栈
- 核心引擎：oh-my-openagent（TypeScript 编写，作为 submodule 引入）
- 前端：Next.js 15 + Tailwind v4 + opennextjs-cloudflare，部署于 Cloudflare Workers
- 集成方式：Codex 插件市场安装或 npx 脚本，通过 hooks 注入技能与代理角色
- 命令层：暴露 `$ulw-plan`、`$start-work`、`$ulw-loop` 等 OmO 原生命令

## 核心能力
- **项目记忆**：`$init-deep` 自动生成分层 `AGENTS.md`，为后续智能体提供代码库上下文
- **战略规划**：`$ulw-plan` 生成决策完备的计划文档，不触及产品代码
- **执行与验证**：`$start-work` 按计划执行直到全部完成；`$ulw-loop` 循环执行并验证结果证据，非空口承诺
- **多模型路由**：根据任务类别自动选择模型（如 `gpt-5.4-mini` 做小编辑，`gpt-5.2` 处理复杂逻辑，`gpt-5.3-codex` 做工程任务），节省配额
- **子代理角色**：内置 explorer、librarian、plan、momus、metis 等角色，可通过 `agent_type` 参数调用
- **技能生态**：review-work、remove-ai-slops、frontend-ui-ux、LSP、AST-grep 等开箱即用
- **诊断与修复**：`npx lazycodex-ai doctor` 检查安装健康状态

## 适用场景
- 使用 Codex 或 Claude Code 的开发者，希望引入规范化的规划-执行-验证开发流程
- 大型代码库需要多智能体协同分析、重构或新功能开发
- 对 OmO 感兴趣但被其配置复杂度劝退的用户
- 需要模型配额管理、降低 API 开销的团队

## 同类对比
- **vs 原生 OmO**：LazyCodex 是做“发行版”工作，封装了 Codex 的插件接口与配置，免去手动设置 hooks、agent 角色、技能等步骤
- **vs oh-my-codex**：灵感来源，但 LazyCodex 是完整的重新实现，并实时同步 OmO 最新版本
- **vs Cursor/Copilot**：这些侧重于代码补全和聊天，而 LazyCodex 提供自主规划、执行、验证的智能体流水线，适合更为复杂的工程任务

## 版本动态
当前版本 v4.13.0（2026-06-22），同步 OmO v4.13.0 市场载荷。更新亮点包括：Ultimate Browsing/Insane Search 共享技能、Ultraresearch 验证门更新、CodeGraph 改进、Team Mode、稳定性强化。项目活跃，由 Sisyphus Labs 的 Jobdori 持续维护。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供具体 benchmark 数据（如 SWE-bench 得分）证明智能体效率；模型路由的实际成本节省案例缺失；对 Claude 模型的具体支持情况和兼容性未深入说明（仅提及历史被封）；未说明 API 密钥等环境变量的配置方法