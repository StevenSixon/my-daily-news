## 它是什么

Cyrene-Agent 是一个以《崩坏：星穹铁道》角色“昔涟（Cyrene）”为核心的 Windows 桌面 AI 伴侣。它不只是桌宠，还内置了完整的 Agent 工作流（CITA→Action Gate→Native FC→Execution Policy→Tool Runtime→Soul 回复），并自研 DMAE 记忆引擎实现分层长期记忆。项目用 TypeScript + Electron 构建，Live2D 由 pixi-live2d-display 驱动，模型推理靠本地 Transformers（@xenova），工具覆盖文档、搜索、音乐、MCP 扩展等，同时支持飞书和微信 iLink 接入。

## 为什么火

项目把“角色化陪伴”和“结构化 Agent”两大需求合体了：桌面宠物的 Live2D 互动性比纯聊天框更有沉浸感，而可信任的工作模式（Work）又让昔涟能真正帮你干活，如写文档、查天气、发邮件，比常规聊天机器人实用。分层记忆（L0/L1/L2 + DMAE Worldbook）让它能记住你的偏好，随使用时间显得更懂你。对开源社区而言，它完整展示了 Electron + LangGraph 模式的桌面 Agent 参考实现，还有独立开发的 CITA 上下文引擎和多重校验机制，可玩性和参考价值都很高。

## 技术栈

- 运行环境：Node.js 24 LTS + Electron 43
- 语言：TypeScript 5
- 构建：Vite 5
- 界面：HTML/CSS + Pixi.js 7 + Chart.js
- Live2D：pixi-live2d-display 0.5.0-beta + Cubism Core
- Agent 工作流：LangGraph + Structured Output + Native Function Calling
- 工具扩展：@modelcontextprotocol/sdk
- 记忆与检索：本地 Embedding（@xenova/transformers，BGE-M3）+ BM25 + 自研 Cross-Encoder Reranker
- 桌面自动化：Playwright + @nut-tree-fork/nut-js
- 语音：TTS/ASR + silk-wasm
- 外部渠道：飞书 OpenAPI、微信 iLink
- 原生截图：Rust + DXGI Desktop Duplication/Direct2D / GDI + NDJSON IPC
- 测试：Vitest 4

## 核心能力

1. **Chat 模式**：纯角色化聊天，不暴露工具，人格化回复结合记忆和用户风格。
2. **Work 模式**：完整 Agent 工作流，经上下文理解、行动决策、参数生成、安全校验后执行工具，并根据真实结果回复。
3. **长期记忆**：L0（核心画像）/L1（近期状态）/L2（长期经历）+ DMAE Worldbook，支持记忆冲突检测、证据链追溯。
4. **桌面陪伴**：Live2D 显示、表情动作联动、智能表情包、气泡互动、多窗口独立运行。
5. **语音交互**：实时 ASR + 多 TTS 引擎 + 语音通话，带 VAD 静默检测。
6. **工具生态**：联网搜索、文件处理、文档生成（Word/Excel/PDF）、生活服务、网易云音乐控制、MCP 服务器扩展。
7. **多平台接入**：桌面端、飞书、微信 iLink 共享人格和记忆。
8. **安全与模型适配**：多厂商分级 Structured Output 兼容，API Key 部分用 Electron safeStorage 加密，飞书密钥完全加密。

## 适用场景

- 想要一个既能闲聊又能自动干活（查信息、做表格、放音乐）的桌面智能助手。
- 对 Live2D 角色陪伴有执念的二次元/崩铁玩家。
- 研究 Electron 下 AI Agent 架构的开发者，特别是本地记忆、工具调用和多渠道接入的参考实现。
- 愿意折腾 Windows 环境、自行配置 LLM API 的 DIY 用户。

## 同类对比

比纯聊天式桌面宠物（如某桌宠插件）多了可信的 Agent 执行链和工具生态；比只做 Agent 框架的项目（如 LangChain/Agent 模板）多了完整的 Live2D 交互和角色人格；和闭源桌面 AI 助手（如 Windows Copilot）比，开源、可定制、用自己选择的模型，隐私可控。缺点是仅 Windows 平台，部分功能（微信 iLink、RAG、主动聊天）仍实验性，且资源占用不低。

## 版本动态

最近更新在 2026-07-27，项目处于活跃开发状态。最新 Release 是 BGE-M3 嵌入模型包（570 MB），推荐安装以启用贴纸语义匹配等增强功能。从 commit 频率看，作者在持续迭代 Work 流程、工具和文档。
---

## ℹ️ 置信度与信息盲区

- 置信度：**medium**
- 信息盲区：缺少性能基准和实际响应延迟数据；RAG 文档知识库和 MCP 扩展仍标记为实验性，未说明稳定场景；微信 iLink 和主动聊天属于实验性，具体使用限制未详细说明；macOS/Linux 兼容性未完整验证，透明窗口可能存在问题；没有提供已适配模型厂家的明确测试通过率或兼容性表格细节