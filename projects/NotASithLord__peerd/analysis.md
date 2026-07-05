## 它是什么
peerd 是一个浏览器扩展（Chrome/Firefox），将AI代理循环完全运行在用户浏览器内。它利用浏览器原生安全模型（V8隔离区、WebCrypto、沙箱iframe）构建多个隔离的“演员”（actor），由中心编排器（orchestrator）委托任务，实现安全的多环境代理操作。支持直接读取/驱动标签页、启动沙箱计算（JavaScript Notebook、WebAssembly Linux VM）、构建小型客户端应用，并在预览版中提供基于WebRTC的点对点代理间通信和共享网络。用户自带模型密钥（BYOK），支持 Anthropic、OpenRouter 以及本地 Ollama。所有数据存储在本地加密保险库，无遥测、无后端，数据路径中无云组件。

## 为什么火
- **无后端隐私**：完全本地运行，消除了对第三方服务器的信任依赖。
- **浏览器原生安全**：利用 V8 隔离区、WebCrypto、同源策略等成熟平台能力，而非自行实现加密或沙箱。
- **多环境代理**：一个扩展统一管理多个浏览器标签页、Linux VM、笔记本和应用的执行。
- **创新隔离设计**：持有密钥的中心代理无法触碰任何环境；每个环境由独立的演员代理操作，仅返回受控摘要，防止提示注入扩散。
- **开放且可审计**：无构建步骤，纯原生 JavaScript，便于审查。

## 技术栈
- 核心语言：纯 JavaScript (ES2024+)，无 TypeScript、无构建、无打包器。
- 浏览器平台：Manifest V3，Service Worker，offscreen 文档，Web Workers，chrome.debugger（预览版）。
- 沙箱技术：V8 隔离区（Chrome）、Worker 堆内存隔离、opaque-origin iframe、WebAssembly (Linux VM)。
- 加密：WebCrypto API，WebAuthn 密钥解锁，本地保险库。
- 模型适配：Anthropic、OpenRouter、Ollama。
- P2P：WebRTC 数据通道（预览版）。
- 代码组织：五个模块（peerd-provider, peerd-egress, peerd-engine, peerd-runtime, peerd-distributed），每个模块通过 `index.js` 暴露公共 API。

## 核心能力
- **代理编排**：中心代理将目标委托给特定演员（web/WebVM/Notebook/App），接收 fenced 摘要，自身无直接环境操作工具。
- **表格驱动**：可读取和操作任意标签页，通过观察页面实际变化判断操作成功。
- **沙箱计算**：一键启动 JavaScript 笔记本、WebAssembly Linux VM 或客户端应用，支持从页面提取数据、运行代码并返回结果。
- **安全防线**：文件读取和运行输出经过 `wrapUntrusted` 隔离；所有出站请求经 `safeFetch`/`webFetch`，禁止原生 `fetch`；egress 模块作为唯一出口，实施允许列表和审计。
- **P2P 网络（预览）**：引入 `dweb actor`，管理发现、安装、分享、信誉账本，仅接受通知，不会由外部消息触发主动操作。
- **数据本地化**：聊天记录、密钥、审计日志全部加密存储在本地，支持导出/导入。

## 适用场景
- 需要高频操作浏览器页面的自动化任务（数据抓取、表单填写、测试），且注重隐私。
- 希望在本地运行 AI 代理，避免将浏览上下文发送到云端的开发者。
- 探索浏览器原生代理框架、沙箱计算和 P2P 去中心化应用的极客。
- 使用 BYOK 进行研究和原型设计，不想依赖固定后端的 AI 工具。

## 同类对比
- **类似浏览器代理工具（如 MultiOn、Agent-E、Browserbase）**：大多依赖云端后端或浏览器服务，peerd 完全本地运行，隐私性更强，但也受限于单机资源。
- **类似本地化 AI 工具（如 Ollama + 简单脚本）**：peerd 提供了结构化的多演员隔离和编排，集成更多浏览器控制能力，复杂度更高但安全性更强。
- **自建代理框架（如 LangChain 浏览器工具）**：通常运行在 Node.js 进程内，缺乏浏览器原生安全隔离，peerd 直接在扩展上下文利用平台能力。
- **优势**：零后端部署，数据主权完全在用户手中；隔离设计有效缓解提示注入风险；模块化设计透明可审。
- **劣势**：处于 0.x 实验阶段，界面和 API 可能频繁变更；Firefox 支持仍在完善；依赖浏览器扩展权限，对非技术用户门槛较高。

## 版本动态
- 最近发布：v0.2.2 (2026-07-04)，引入了 dweb actor 预览、修复了文件读取隔离漏洞、优化了演员回复的可视化和 Notebook 热力图图表。
- 状态：0.x 实验 Beta，作者声明可能会有破坏性更改，不建议在生产环境盲目使用。
- 仓库活跃度：Star 303，开发活跃，提交频繁。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**