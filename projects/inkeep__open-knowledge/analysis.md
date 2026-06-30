## 它是什么
OpenKnowledge 是一个面向 AI 代理的知识库编辑环境，提供所见即所得的 Markdown 编辑，并与 Claude Code、Codex、Cursor 等 AI 编码助手深度集成。你可以把它理解为“Notion 加上 VSCode 式的 AI 协同”，文件以本地 Markdown/MDX 存放，支持通过 MCP 或 CLI 被任何代理调用。

## 为什么火
在 LLM 代理逐渐成为开发常态的背景下，一个能为代理提供结构化知识库、且代理又能直接参与编辑的工具存在空白。OpenKnowledge 提供了开箱即用的 MCP 服务器、技能注册和代理搜索，让代理可以像人一样阅读、链接、修改笔记。同时它完全本地优先，无需云账号，用 Git 做团队同步，契合极客的隐私和掌控需求。其 Star 增长快速，社区活跃。

## 技术栈
- 前端/编辑器：TypeScript, Next.js, Tailwind, MDX 支持
- 桌面端：macOS 原生应用
- 后端/CLI：Node.js（需要 24+），通过 npm 全局安装 CLI
- 集成：MCP 协议、Claude Code/Codex/Cursor 的 harness 配置自动注入
- 同步：底层使用 Git/GitHub，实现无代码的团队共享与自动同步

## 核心能力
- 完全 WYSIWYG 的 Markdown 编辑体验
- 本地知识图谱：文件浏览、反向链接、图视图、全文搜索、标签页
- AI 协同：代理可通过 MCP 搜索、读取、写入、编辑文档；支持技能定义
- 自动集成：`ok init` 会检测本机已安装的 AI harness 并注入 MCP 及技能配置
- 配置安全：修改 harness 配置文件时保留原有格式、注释、键顺序，非破坏式注册
- 附件管理：可设置上传路径为内容根目录或当前文件夹
- 实时索引：文件写入后即刻更新链接图，避免新文档被误报为死链接
- 运行模式：macOS 桌面应用 或 本地 Web UI（通过 CLI 启动）

## 适用场景
- 为 Claude Code 或 Codex 构建项目专属的“第二大脑”，存放需求、设计决策、面试笔记
- 工程团队用 Markdown 写规范，交由代理自动更新、维护知识库
- 个人笔记体系（替代 Obsidian/Notion），同时让本地 AI 助手参与整理
- 需要私有化部署、不依赖云服务的知识管理

## 同类对比
- vs Notion：Notion 是云端服务，AI 功能封闭；OpenKnowledge 本地存储、开源、自由接入任何 MCP 客户端
- vs Obsidian：Obsidian 的 AI 插件多为第三方，集成深度有限；OpenKnowledge 原生设计为代理的可编程知识库
- vs Foam/Dendron：均为 VSCode 内知识管理，但缺少对 MCP 和代理技能的一等支持
- 独特优势：自动扫描本机 AI 工具并注入配置，官方桌面应用与 Web UI 一致，团队共享基于 Git

## 版本动态
最新稳定版 v0.21.0（2026-06-30）：
- MCP 配置写入改为非破坏式，保留 JSON/TOML 格式、注释、BOM 等
- 修复文件监听延迟导致新文档显示为红链的问题
- 新增附件上传路径设置（根目录或当前文件夹）
- 增强 Codex 的 toml_edit 处理，避免 64 位整数和微秒时间被错误标记
- 分享功能开始加入（截断信息显示 sharing r...，可能后续完善）
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提及除 Claude/Codex/Cursor 外的 MCP 客户端测试情况；无性能基准数据（如大型知识库的索引速度）；未说明 Web UI 模式的最低内存/CPU 要求；分享功能（sharing r...）在 Release notes 中被截断，未完全描述