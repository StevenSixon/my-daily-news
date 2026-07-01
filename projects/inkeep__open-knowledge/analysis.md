## 它是什么
OpenKnowledge 是一个 AI 原生的 Markdown 编辑器，定位为“LLM Wiki”和“第二大脑”。它提供本地 macOS 应用和 Web UI，支持真正的所见即所得编辑，并与 Claude、Codex、Cursor 等 AI 桌面应用无缝集成，自动检测并配置 MCP、Skills 等 Agent 能力。项目由 TypeScript 构建，使用 Next.js 作为 Web 框架，通过 Git 实现团队共享和自动同步。

## 为什么火
AI 辅助写作与知识管理需求爆发，但多数工具要么是纯云端的 Notion/AI，要么是 Obsidian 等依赖复杂插件的本地方案。OpenKnowledge 做到了开箱即用的 AI 聊天、终端内协作、文档智能搜索，且完全本地运行、免费开源。它降低了非技术用户用 AI 打理笔记和知识库的门槛，又保留了极客可定制的底层能力（CLI、MCP）。

## 技术栈
- 语言：TypeScript
- 前端框架：Next.js（React）
- 桌面端：未明确技术（可能是 Electron 或 Tauri，依赖 macOS 原生包）
- 存储：本地文件系统，基于 Markdown/MDX
- 同步：Git/GitHub 集成
- AI 集成：直接调用本地 AI Agent CLI（Claude Code、Codex、Cursor 等），支持 MCP 和 Skills

## 核心能力
- **WYSIWYG 编辑**：像 Google Docs 一样编辑 Markdown 文件
- **AI 协同**：选中文本一键发送至 AI Agent，终端内拖放文件直接参与对话
- **Agent 集成**：自动检测已安装的 AI 工具并初始化 MCP/Skills 配置
- **知识图谱**：wiki 链接视图、文件导航、搜索
- **团队共享**：基于 Git 的无代码同步与协作
- **多形态界面**：桌面应用、Web UI、内置 TUI

## 适用场景
- 个人知识管理、编程笔记、技术文档
- 团队共同维护的 LLM 知识库或 Agent 第二大脑
- 需要本地隐私并要求 AI 辅助创作的写作者
- 希望在现有代码库中快速建立文控的开发者

## 同类对比
| 工具 | AI 集成方式 | 本地优先 | 协作 | 开源 |
|------|-------------|----------|------|------|
| OpenKnowledge | 直接联动本地 Agent CLI | ✅ | ✅ (Git) | ✅ |
| Obsidian | 依赖社区插件 | ✅ | 付费同步 | ❌ |
| Notion | 内置云 AI | ❌ | ✅ | ❌ |
| Bear | 基础 AI 助手 | ✅ | ❌ | ❌ |
OpenKnowledge 的最大差异在于将 Agent 视为一等公民，并自动完成环境配置，让文档编辑和 AI 操作自然融合。

## 版本动态
最新稳定版 v0.23.0（2026-07-01）引入了新手引导卡片、终端拖放文件支持、AI 聊天与终端一体化切换按钮，并可根据本机安装的 Claude/Codex/OpenCode/Cursor 自动选择默认 CLI。项目处于活跃开发期，迭代节奏快。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：桌面应用的技术栈未公开（Electron 或 Tauri 等）；未提供性能/资源占用基准；默认 CLI 检测列表是否可扩展未说明；自托管部署的服务器要求未提及；与其他工具的功能详细对比缺失