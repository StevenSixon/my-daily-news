## 它是什么

OpenKnowledge 是一个面向本地 Markdown/MDX 文件的编辑器，提供真实 WYSIWYG 体验，并深度集成了 Claude、Codex、Cursor 等 AI Agent。它定位为“个人第二大脑”和“LLM Wiki”，用户可以用它撰写笔记、工程规格、文档，并允许 AI 代理参与编辑、搜索和知识图谱构建。项目提供 macOS 桌面应用和基于 Next.js 的 Web 界面，通过 CLI（需 Node.js 24+）在 Linux/Windows 上运行。

## 为什么火

- **AI 原生协作**：不单是粘帖对话，而是直接将 AI 代理接入编辑器，像多人协作一样修改文档，符合 LLM 时代的知识工作流。
- **本地优先与自由**：所有文件保留在本地，无需托管，隐私安全；GPL-3.0 许可，源码开放，支持自构建。
- **统一工具链**：将 Obsidian 式的链接/图谱、Notion 的编辑体验、VS Code 式的文件树/终端融为一炉，并支持 MCP 协议和 Agent Skills，智能体可直接操作知识库。

## 技术栈

- 前端/编辑器：TypeScript，基于 Next.js（见 next.config.ts），Tailwind CSS，可能使用 TipTap 或 Slate 作为富文本引擎，实现 WYSIWYG Markdown。
- 桌面应用：用 Tauri 或 Electron 打包（macOS DMG），内部集成 Web UI 和终端。
- 后端/服务：CLI 服务提供本地 Web 服务器，支持 MCP 协议。通过 `@inkeep/open-knowledge-core` 和 `@inkeep/open-knowledge-server` 包组织。
- 同步与协作：底层依赖 Git/GitHub 实现团队共享和自动同步。

## 核心能力

1. **所见即所得编辑**：Markdown 文件编辑如同 Google Docs，避免源码与预览分离。
2. **多代理集成**：支持 Claude Code、Codex、Cursor 和任意 MCP/CLI Agent（如 OpenCode），Agent 可以直接读取、修改文件。
3. **MCP 与 Skills 开箱即用**：自动检测并配置代理工具的技能与上下文，使得知识库成为 Agent 可用的工具集。
4. **知识图谱与搜索**：侧边栏展示 Wiki 链接图，Agentic Search 让代理能检索知识库内容。
5. **团队共享**：基于 GitHub 的用户管理，无代码配置即可实现多人协同，自动同步更改。
6. **嵌入式富组件**：支持 HTML、图表等，方便写技术规格和可视化报告。
7. **双界面**：桌面端内置终端 UI（TUI），同时提供完整 Web 界面。

## 适用场景

- 个人知识管理：构建第二大脑，笔记、想法、读书摘要。
- 技术文档团队：多人协作撰写产品文档、API 文档，并用 AI 辅助生成和维护。
- AI 代理的“长期记忆”：作为 Agent 的持久化知识库，通过 MCP 连接，让 Agent 具备学习和记忆能力。
- 工程规范与设计文档：内嵌图表，AI 辅助起草架构稿。

## 同类对比

- **vs. Notion**：Notion 为云托管，AI 功能收费；OpenKnowledge 本地存储，自由度高，AI 集成更深且免费。
- **vs. Obsidian**：Obsidian 有强大的本地日志和插件系统，但原生 AI 交互弱，WYSIWYG 模式非默认；OpenKnowledge 聚焦 AI 协作与所见即所得，提供类似 Notion 的流畅体验。
- **vs. VS Code + 插件**：VS Code 可编辑 Markdown 并接入 Copilot，但编辑体验仍偏向源码，缺乏无缝的 WYSIWYG 和知识库专用功能（如图谱视图、Wiki 链接自动补全）。

## 版本动态

最新稳定版 v0.19.2 主要修复了“Ask AI”中终端行标签的可访问性，并隐藏了自动生成的 `opencode.json` 配置文件，避免在文件树中干扰用户。项目处于较早期的活跃开发阶段，近期更新频繁，社区通过 Discord 和 X 频道响应问题。
---

## ℹ️ 置信度与信息盲区

- 置信度：**medium**
- 信息盲区：团队共享时 GitHub 同步的具体机制与权限要求未详述；大文件/多文件的性能表现未知；是否支持离线 AI 推理（如本地模型）或仅依赖外部 Agent；桌面应用的技术栈（Tauri/Electron）未说明；没有自托管服务端的更多信息