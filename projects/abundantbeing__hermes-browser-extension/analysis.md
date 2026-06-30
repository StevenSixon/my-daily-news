## 它是什么

Hermes Browser Extension 是一个 Chrome/Edge 等 Chromium 浏览器的侧边栏扩展，专门为 Hermes Agent 运行时设计。它不是独立聊天机器人，而是桥梁，能将当前标签页的标题、URL、选中文字、页面文本、元数据等上下文信息安全地发送给本地或远程的 Hermes 网关，并流式显示回复。

## 为什么火

在 Nous Research 开源的 Hermes Agent 生态中，该扩展填补了「浏览器内直接向 Agent 注入网页上下文」的空白。它以 **本地优先** 和 **标签页作用域隔离** 为特色，支持无页面模式（纯聊天）、跟随活动标签、固定标签等多种上下文策略，避免隐私泄露，非常适合需要利用网页内容进行推理、总结或操作的开发者。

## 技术栈

- 前端：JavaScript (MV3 扩展)，使用 Chrome Side Panel API
- 通信：通过 HTTP REST API 或 WebSocket 连接 Hermes Gateway
- 构建：Node.js，npm 构建脚本
- 安全：只读权限，无调试接口、无 cookies/history 权限

## 核心能力

- 连接本地或远程 Hermes API 服务器，自动同步模型、Skills、Profiles、Sessions
- 上下文作用域控制：Chat only / 跟随活动标签 / 固定标签 / 页面专用模式
- 标签页级消息缓存与会话隔离
- 快速命令：/summarize, /explain, /rewrite, /tabs, /action-items
- “What Hermes saw” 透明度查阅
- 多主题外观，支持语音输入
- 兼容旧版 Hermes 网关的优雅降级

## 适用场景

- 正在使用 Hermes Agent 并希望在不离开浏览器的情况下对话、总结网页、提取信息
- 需要快速将浏览器内容注入 Agent 工作流，例如让 Agent 根据当前页面内容生成报告或回答
- 在多个标签页之间切换时保持独立的会话上下文

## 同类对比

相较于通用的浏览器 AI 助手（如 ChatGPT 侧边栏、Perplexity 等），Hermes 扩展更深耦合 Hermes Agent 生态，支持本地模型和工具链，且不依赖云端服务，隐私控制更严格。相较于其他浏览器 Agent 扩展（如 Page Assist），它更聚焦只读上下文，未包含网页自动化操作。

## 版本动态

最新 v0.1.7 强调标签页作用域、纯聊天模式、上下文范围菜单和更准确的上报。项目仍处于公开 alpha 阶段，尚未上架应用商店，需手动加载。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供性能基准或资源消耗数据；需依赖 Hermes Agent 安装与配置，入门门槛较高；未说明对 Firefox/Safari 的支持计划