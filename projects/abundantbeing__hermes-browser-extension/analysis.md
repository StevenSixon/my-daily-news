## 它是什么
一个浏览器侧边面板扩展，为 [Hermes Agent](https://hermes-agent.nousresearch.com/docs) 提供前端界面。它不是独立的聊天机器人，而是将当前浏览页面的上下文（标题、URL、选中文本、可读内容等）安全地发送到用户本地或远程运行的 Hermes 运行时，并流式展示 Agent 的回复。

## 为什么火
Hermes Agent 是 Nous Research 推出的本地优先、可组合的 AI Agent 框架，近期关注度很高。该扩展填补了浏览器与 Agent 之间的鸿沟，让用户在日常浏览中直接利用本地 Agent 的模型、工具、技能和记忆，且所有上下文处理都在用户控制的网关内完成，契合隐私优先和自托管的趋势。

## 技术栈
- JavaScript/TypeScript 构建，使用 Manifest V3 规范
- 基于 Chrome/Edge 的 Side Panel API 实现侧栏
- 与 Hermes Gateway 的 REST API 通信（`/v1/*`, `/api/*`），支持 WebSocket 仪表板模式
- 面向 Hermes 的本地/远程 API 服务器，默认地址 `http://127.0.0.1:8642`
- 前端主题系统支持 6 种预设（Nous, Midnight, Ember, Mono, Cyberpunk, Slate）及明暗模式

## 核心能力
- **上下文捕获**：自动提取当前标签页标题、URL、打开标签列表、选中文本、页面可读正文、元数据、标题、表单、链接和按钮等，并标记为不可信内容发送给 Hermes
- **能力协商**：通过 `/v1/capabilities` 检测 Hermes 网关支持的功能，对不支持的路线提供明确的降级提示（如语音转录回退到浏览器 Web Speech）
- **连接模式**：支持本地 API 服务器、远程 API 服务器（通过 HTTP/HTTPS）以及仅仪表板 WebSocket 模式
- **安全控制**：API 密钥掩码显示，可一键清除；提供“What Hermes saw”收据，展示每次发送的上下文载荷；仅使用最小权限（无调试器、无原生消息、无下载/历史记录权限）
- **主题与体验**：类桌面应用的样式设置，流式响应展示，并支持语音输入（Hermes STT 或浏览器语音）

## 适用场景
- 希望通过浏览器即时让本地 Hermes Agent 分析网页、提取信息或执行与研究相关的 Agent 任务的开发者
- 注重隐私、不想将浏览数据发送至第三方云端的用户
- 已经搭建好 Hermes 环境，需要简便的浏览器原生交互界面的场景

## 同类对比
与通用的 AI 侧边栏扩展（如 ChatGPT 浏览器插件）不同，Hermes Browser Extension 专为 Hermes Agent 设计，不去依赖云端 API，所有模型调用和工具执行都在用户控制的本地或远程运行环境中完成。它不直接操纵页面，而是作为“只读上下文桥梁”，更符合安全准则。当前其他本地 Agent 框架（如 Open Interpreter、AutoGPT 等）尚未推出类似的官方浏览器扩展，该扩展填补了社区生态的一块空白。

## 版本动态
最新版本 v0.1.5（2026-06-27）仍处于公开 alpha 阶段，主要强化了兼容性与信任机制：新增能力面板、连接流程优化、语音能力门控、令牌安全 UI、上下文收据等功能。已有 6 次后续补丁提交和 2 个合并 PR，1 位社区贡献者参与，并增加了静态检查。目前尚未上架 Chrome Web Store，需手动加载。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**