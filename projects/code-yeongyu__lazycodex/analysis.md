## 它是什么
LazyCodex 是将 OmO（oh-my-openagent）代理框架打包为 Codex 平台的可安装插件，提供 AI 驱动的代码库规划、执行与验证工具链。类似 LazyVim 为 Neovim 提供预配置环境，LazyCodex 让 Codex 用户无需手动编排多个代理即可享受 OmO 的代理能力。

## 为什么火（Star 1565）
OmO 本身以 60k Stars 和质量著称，曾因过度使用 Anthropic 模型导致第三方客户端被屏蔽，其代理流程极其严格。LazyCodex 通过一行命令将这套高质量代理系统引入 Codex，吸引了需要自动化复杂代码库任务的开发者。社区对“零配置多代理”方案的需求推动了其热度。

## 技术栈
- 核心引擎：OmO（TypeScript）
- 分发层：LazyCodex（TypeScript）
- 前端站点：Next.js 15 + Tailwind v4，部署于 Cloudflare Workers
- 集成方式：Codex 插件系统，通过 CLI 安装
- 模型路由：支持 OpenAI GPT-5.x 系列模型，根据任务类型自动分配
- 代理角色：Sisyphus、Hephaestus、Oracle 等多角色编排

## 核心能力
- **代理命令**：`$ulw-loop`（循环至验证完成）、`$ulw-plan`（战略规划）、`$start-work`（执行计划）
- **技能系统**：包括 `$init-deep` 生成项目记忆（AGENTS.md），代码审查、前端打磨、编程规范等
- **多代理并行**：能在 Codex 中调用子代理角色（explorer, librarian 等）同时工作
- **模型智能路由**：根据任务复杂度选择不同 OpenAI 模型，节省配额
- **零配置**：默认值合理，开箱即用
- **诊断工具**：`npx lazycodex-ai doctor` 检查安装健康

## 适用场景
- 需要在 Codex 中管理大型、复杂代码仓库的开发者
- 希望自动化项目上下文记忆、多步骤规划与验证的团队
- 想利用多代理协作完成调研、重构、修复等任务的个人或组织

## 同类对比
与 oh-my-codex 等项目相比，LazyCodex 基于 OmO 完整代理框架，提供更全面的规划、执行和验证闭环，而非简单命令集。相对于手动配置 OmO，它大幅降低了进入门槛。

## 版本动态
仓库最近活跃（2026-06-20），v4.12.1 刚发布，同步自 OmO v4.12.1。项目仍在持续迭代。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供与类似工具（如 oh-my-codex）的详细性能对比；未说明 Codex 的最低版本要求；无具体 benchmark 数据