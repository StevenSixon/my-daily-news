## 它是什么

一个 Claude Code 技能（同时支持 Codex、Gemini、Cursor、Windsurf、Cline、Copilot 等 30+ 代理），通过注入压缩规则，强制代理**去除冗余用语，仅保留技术实质**，将输出 token 降低 65–75%，但完全不损失代码、命令、路径等准确信息。

核心哲学：**“why use many token when few do trick”**。提供 4 档压缩等级（lite / full / ultra / 文言文），支持多语言输出压缩，并能压缩记忆文件（CLAUDE.md）、提交信息、PR 评审等，形成一套完整的代理输出瘦身体系。

## 为什么火

- **省钱省时**：API 输出成本直降 65%，回复速度提升约 3 倍，上下文窗口更耐用。
- **真实可信**：README 中给出 10 项任务实测数据，平均从 1214 token 降至 294 token，并提供 `benchmarks/` 复现脚本。
- **安装无痛**：一条 curl 命令自动检测已安装代理并注入规则，多平台开箱即用。
- **社区 meme 化 + 学术背书**：引用 2026 年论文《Brevity Constraints Reverse Performance Hierarchies》，表明精简有时反而提升准确性。

## 技术栈

- 语言：JavaScript（Node.js 脚本）
- 安装方式：bash / zsh / PowerShell 脚本，通过 curl 或 irm 拉取
- 规则存储：Markdown 技能文件（SKILL.md）、钩子脚本、环境标记文件
- 集成方式：利用各代理的自定义技能/插件机制（Claude Code skills、Codex plugins、Cursor rules 等）
- 分发：GitHub Release 标签 v1.9.0（不可变安装），含 SHA-256 完整性校验

## 核心能力

- `/caveman [lite|full|ultra|wenyan]` ：切换压缩级别，会话内生效
- `/caveman-commit`：生成 ≤50 字符的约定式提交信息
- `/caveman-review`：单行 PR 评论（位置 + 严重度 + 问题 + 修复）
- `/caveman-stats`：展示当前会话及累计节省 token 数、美元估值，可生成可分享的文字
- `/caveman-compress <file>`：将记忆文件（如 CLAUDE.md）压成原始人风格，平均再省 46% 输入 token
- `caveman-shrink`：MCP 中间件，压缩任何 MCP 服务器的工具描述
- `cavecrew-*`：压缩版子代理（investigator/builder/reviewer），让主上下文存活更久

## 适用场景

- 高频使用 AI 编程助手回复场景（日常编程、Code Review、Debug）
- 希望降低 API 成本、加速响应、减少阅读时间的个人或团队
- 多代理环境下统一输出风格，减少上下文膨胀
- 作为 Claude Code 记忆文件（CLAUDE.md、project-notes.md）的定期压缩工具

## 同类对比

- **直接提示“回答简洁”**：效果有限且不稳定，caveman 通过规则注入实现持续、可靠的压缩，且与最新研究结果一致（约束指令可提升准确性）。
- **其他 token 压缩工具**：多数侧重输入压缩（如摘要记忆），caveman 专注**输出端压缩**，并与 `caveman-compress` 形成输入输出双重瘦身组合。
- **与完整代理 caveman-code**：本仓库是输出压缩技能，其同门项目 [caveman-code](https://github.com/JuliusBrussee/caveman-code) 是全方位压缩的终端编码代理，token 消耗更少。

## 版本动态

- 最新版 v1.9.0（2026-06-12）引入固定标签安装 + SHA-256 完整性校验，修复文档站 DOM XSS
- 针对 opencode 的兼容性从“完全不可用”修至全线跑通（生命周期钩子、命令扩展、会话标记等问题同步修复）
- 新增仓库级配置 `.caveman/config.json`，支持团队级默认模式
- 增加自然语言触发词（“less tokens”“be brief”等）
- 安装器增加 Copilot 检测路径修复
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**