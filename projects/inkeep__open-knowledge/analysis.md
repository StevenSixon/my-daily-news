## 它是什么
OpenKnowledge 是一个本地优先的所见即所得 Markdown 编辑器，专为个人笔记、规范文档和 LLM Wiki 打造。它原生化集成了 Claude、Codex、Cursor 等桌面 AI 应用，并支持通过 MCP/CLI 接入任意代理（如 OpenCode）。提供 macOS 桌面应用和跨平台本地 Web 应用两种使用方式，数据通过 Git/GitHub 实现无代码团队共享。

## 为什么火
随着 AI 代理人工具普及，开发者需要一种既能保留本地数据主权，又能无缝与多个 LLM 协作的笔记环境。OpenKnowledge 直接在编辑界面嵌入「Ask AI」和代理选择器，让文档撰写、知识库维护和代理间协同变得像原生功能一样自然，避免了在多个工具间切换。初期已在极客圈获得关注，Star 增长迅速。

## 技术栈
- **语言**：TypeScript
- **前端**：基于 Next.js（推断自项目文件结构）的 Web 编辑器，桌面应用可能为 Electron 或类似 Web 容器（未官方说明）
- **核心**：本地 Markdown 文件存储，WYSIWYG 编辑引擎（富文本转 MD），MCP 协议集成，agent skills 框架
- **分发**：macOS DMG、npm 全局安装包

## 核心能力
- **真正的 WYSIWYG**：编辑体验类似 Google Docs/Notion，实时渲染 Markdown
- **多 AI 代理协作**：内置 Claude、Codex、Cursor、OpenCode 的快捷入口，支持任意 MCP 兼容代理
- **Agent Skills & 搜索**：代理可通过 skills 执行操作，支持对知识库的智能检索
- **无代码共享与同步**：底层使用 Git/GitHub 自动同步，团队可共同编辑
- **嵌入式富组件**：可插入 HTML 和可视化组件，适合工程技术规范与报告
- **终端 UI（TUI）**：桌面应用内置 TUI，Web 版也有完整 UI

## 适用场景
- 个人第二大脑与知识管理
- 技术团队编写协同规范、架构文档
- LLM 代理的知识基座（LLM Wiki），用于代理间共享上下文
- 带 AI 辅助的快速笔记与会议记录

## 同类对比
- **vs Obsidian**：Obsidian 依赖社区插件实现 AI，体验割裂；OpenKnowledge 原生集成，WYSIWYG 更现代
- **vs Notion**：Notion 为云端优先，AI 功能付费；本工具本地优先，开源且免费（GPLv3）
- **vs Typora**：Typora 无 AI 集成，仅作编辑器
- 优势是开箱即用的多代理协作与本地数据控制，劣势需依赖外部桌面 AI 应用本身

## 版本动态
- 当前稳定版 v0.19.2（2026-06-26），刚从 beta 版晋升
- 近期主要修护：统一「Ask AI」代理选择器标签，隐藏 OpenCode 配置文件以避免干扰
- 项目年轻（首次提交 2026-06-03），迭代速度快，表明社区或团队活跃
---

## ℹ️ 置信度与信息盲区

- 置信度：**medium**
- 信息盲区：未说明桌面应用的底层构建方式（Electron/Tauri/原生）；没有性能或资源占用基准数据；离线功能程度未知（AI 代理显然需联网，但编辑器自身是否完全离线未提及）；移动端支持情况未披露；MCP 和 skills 的具体能力范围未详细展开