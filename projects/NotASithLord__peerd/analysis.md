## 它是什么
peerd是一个浏览器扩展（Chrome/Firefox），将完整的AI Agent循环直接运行在浏览器运行时中。它可以读取和操控标签页，在WebAssembly沙箱中启动JS笔记本或Linux虚拟机，并通过WebRTC实现Agent间P2P通信。所有数据路径无后端、无遥测，用户自带模型密钥（Anthropic/OpenRouter/Ollama等），安全性建立在浏览器原生隔离机制（V8 isolate、WebCrypto、iframe沙箱）之上。

## 为什么火
当前大多数AI Agent方案需要云端服务器处理用户数据和API密钥，存在隐私和延迟问题。peerd完全运行在用户机器上，密钥加密存储于本地vault，Agent循环在Service Worker中编排，实际环境操作由隔离的Actor执行，原始页面内容不会进入持有密钥的上下文。这种**安全边界由浏览器平台强制**的设计吸引了注重隐私和自主控制的开发者。同时，它在浏览器内提供完整的沙箱计算（Linux VM、笔记本、客户端应用），填补了浏览器Agent能力的空白。

## 技术栈
- **前端运行时**：纯Vanilla JS (ES2024+)，ES模块，无TypeScript、无构建步骤、无npm依赖
- **浏览器平台**：Manifest V3，Service Worker作为编排器，V8 isolate for Workers
- **安全模型**：WebCrypto、WebAuthn passkeys、Subresource Integrity、opaque-origin iframes
- **沙箱**：WebAssembly (WASM) Linux VM、JS notebooks、客户端app
- **对等网络**：WebRTC、P2P agent-to-agent通信（预览通道）
- **可扩展性**：模型适配器（Anthropic, OpenRouter, Ollama），安全出口网关（egress allowlist），审计日志

## 核心能力
- **Agent循环**：驱动标签页，执行click、输入、导航，并观察页面实际变化判定成功
- **沙箱执行环境**：创建JS笔记本、WebVM、客户端应用，每个环境由独立Actor隔离
- **P2P共享**：通过WebRTC mesh进行agent间对话，支持线程化对话和回复授权
- **安全守护**：密钥仅存于vault（加密），所有外发请求经安全网关卡点，审计日志带哈希链防篡改
- **模型灵活**：支持闭源/开源/本地模型，一键切换，每会话选模型
- **语音输入**（Goal mode）、技能系统、记忆Review等高级功能

## 适用场景
- 自动化网页操作（如填表、数据抓取）且不希望数据离开本机
- 本地开发环境中的辅助编程与探索，利用浏览器内置沙箱运行不安全代码
- 学术/安全研究中的可控浏览器代理实验
- 去中心化应用（dweb）的早期试验，构建Agent-to-Agent的P2P协作

## 同类对比
- **Open Interpreter / TaskWeaver**：通常依赖Python后端和云端模型，peerd完全在浏览器内运行，无安装负担
- **ChatGPT插件/Claude desktop agent**：绑定特定模型，存在遥测，peerd是BYOK且代码开源可审计
- **其他浏览器自动化扩展**：多仅支持简单脚本，peerd提供了完整Agent循环和隔离安全模型
- **Khoj**：本地个人搜索Agent，但peerd更侧重浏览器驱动和P2P计算共享

## 版本动态
- 当前0.x实验beta，v0.2.5于2026-07-06发布
- 安全加固：审计日志完整性、会话授权Origin限制、传输导入门控
- 新增P2P mesh中的持久线程对话（预览），per-conversation回复授权
- 破坏性变更可能，存储格式未冻结，无V1承诺
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供基准测试数据（如Agent任务成功率、延迟对比）；与同类工具（Open Interpreter、AutoGPT等）的直接对比未给出；dweb预览通道的稳定性和规模限制未量化；移动端支持状态未说明；沙箱计算环境的性能上限（如WebVM可分配内存）未明示