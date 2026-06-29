## 它是什么
OpenKnowledge 是一个漂亮的本地 Markdown/MDX 编辑器，定位为“LLM Wiki”与第二大脑。它提供真正的所见即所得编辑，同时内建与 Claude、Codex、Cursor 等桌面 AI 代理的协作能力，让 AI 像同事一样直接改写文件。

## 为什么火
- 填补了 Obsidian/VSCode 等编辑器与 AI 对话式交互之间的断层：编辑器内嵌 MCP、Skill 和代理搜索，AI 可主动参与知识整理。
- 全本地运行，免费、隐私，数据只是你文件夹里的 Markdown。
- 桌面端（macOS）+ Web 端统一体验，支持 Git 同步与团队分享，兼顾单人与协作场景。

## 技术栈
- 前端：TypeScript + Next.js（Web 端），Tailwind CSS。桌面应用技术未披露（猜测 Electron 或 Tauri）。
- 核心：自有 `@inkeep/open-knowledge-core` 与 `@inkeep/open-knowledge-server` 包，提供 CLI 与服务端。
- AI 集成通过 MCP 和自定义 Skill 文件实现，与 Claude Desktop、Codex、Cursor 对接。

## 核心能力
1. **完整 WYSIWYG**：像编辑 Google Doc 一样编辑 Markdown，渲染与编辑合一。
2. **AI 协同**：通过 `ok cowork` 等命令构建 Skill 包，手动导入至 Claude 等桌面 APP，让 AI 在上下文内读写你的知识库。
3. **扩展与嵌入**：支持 MDX 组件、嵌入式 HTML，适合工程规范、数据报告。
4. **终端内嵌**：桌面应用内置终端面板，方便命令行操作。
5. **项目自动配置**：`ok init` 检测本机已有代理并自动注入 MCP/Skill 配置。
6. **团队共享**：基于 Git/GitHub 实现无代码同步与分享。

## 适用场景
- 个人知识管理（PKM）与第二大脑
- LLM 的知识底座（Wiki）供代理检索
- 工程团队的技术规范、设计文档，配合 AI 评审
- 已有 Obsidian 等 Vault 的增强，可叠加 AI 能力

## 同类对比
- **vs Obsidian**：Obsidian 侧重双向链接与插件生态，OpenKnowledge 自带 AI 原生集成，无需额外配插件。
- **vs Notion**：Notion 在线重度，不便本地文件级控制；OK 全本地、Markdown 文件透明，可版本控制。
- **vs VSCode + AI 插件**：VSCode 是代码编辑器，OK 专为知识文档优化，编辑体验更接近 Word。
- **vs 其他 AI 笔记工具**：多数是云端 AI 生成摘要，OK 强调 AI 作为合作者直接参与编辑，且完全本地化。

## 版本动态
最新 v0.20.0 稳定版已整合之前 beta 的多个修复：
- 命令隐藏优化，`ok install-skill` 更名为隐藏的 `ok cowork`，避免误导自动安装。
- 修复 git worktree 子文件夹项目创建错误。
- 阻止同一文件双开标签页，改为聚焦已有标签。
- 桌前终端引入，方便不离开编辑器执行命令。
表明项目正在打磨桌面集成与工作流稳定性。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：桌面应用技术栈未披露（Electron / Tauri 等）；MCP 和 Skill 的具体能力边界、可扩展性及安全性未详细说明；团队共享基于 GitHub 同步，但本地多人同时编辑的冲突处理策略未提及；无性能基准或大知识库处理能力数据；终端内嵌功能的具体实现（PTY？）未知