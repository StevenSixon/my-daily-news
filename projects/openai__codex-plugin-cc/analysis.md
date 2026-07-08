## 它是什么
一个 Claude Code 插件，通过 `/codex:review` 等命令在 Claude Code 内直接调用本地 Codex CLI，实现代码审查、对抗性评审、任务救援、会话转移等能力。所有操作经过 Codex 应用服务器，使用相同的本地认证和配置。

## 为什么火
仓库星数 26k+ 说明大量开发者希望结合 Claude 和 Codex 的优势，在熟悉的 Claude Code 流程中引入 Codex 的代码审查和后台任务处理，解决单一模型短板。

## 技术栈
- 语言：JavaScript
- 运行时：Node.js 18.18+
- 依赖：本地安装的 `@openai/codex` CLI、Claude Code 插件系统
- 配置：继承 `config.toml`（用户级或项目级）

## 核心能力
- **代码审查**：`/codex:review` 普通审查，`/codex:adversarial-review` 可定制的挑战性审查（质疑设计决策、风险区域）
- **任务委托**：`/codex:rescue` 将问题交给 Codex 调查修复，支持模型和努力程度选择
- **后台与状态管理**：`--background` 异步执行，`/codex:status` 查看进度，`/codex:result` 获取结果，`/codex:cancel` 取消
- **会话转移**：`/codex:transfer` 将 Claude Code 对话上下文导入 Codex 继续
- **审查门**：可选的 Stop 钩子，在 Claude 生成响应后自动运行 Codex 审查并阻止有问题的输出
- **环境设置**：`/codex:setup` 检查安装、登录、管理审查门开关

## 适用场景
- 团队希望用 Codex 做上线前多角度代码审查
- 开发者想在 Claude Code 中处理复杂 bug 时委托给 Codex 节省令牌或利用不同模型
- 长运行任务（如对抗性审查、大规模调查）放入后台异步处理
- 在不同 AI 工具间保持会话连续性

## 同类对比
- 与独立使用 Codex CLI 相比：无需离开 Claude Code，审查结果直接在 Claude 上下文中可见
- 与仅用 Claude 内置审查相比：引入 Codex 特有的对抗性审查和任务救援能力，多模型协作
- 区别于纯 Claude 插件生态：首次深度整合第三方 AI 工具，展示了插件系统的可扩展性

## 版本动态
最新 v1.0.6（2026-07-08）移除了 git 命令的 shell 扩展，提升安全性；持续小幅迭代，社区活跃。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供性能基准数据（审查耗时、资源占用）；未说明与原生 Codex CLI 审查结果的差异；未提及安全审计或权限控制细节