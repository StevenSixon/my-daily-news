## 它是什么
OmniRoute 是一个本地优先的开源 AI 网关，提供单一 `/v1` 端点接入 **231+ 个大模型提供商**（含 90+ 免费层），并自动完成故障转移、成本优化和 token 压缩。它可以把 Claude Code、Codex、Cursor、Cline 等工具无缝对接到免费/廉价的 Claude、GPT、Gemini 等模型，而无需为每个工具单独配置 API 密钥。

## 为什么火
- **免费聚合**：声称每月提供约 16 亿免费 token，去重统计免费池，不夸大。
- **极致压缩**：RTK + Caveman 堆叠压缩技术，在工具调用密集场景可节省 15–95% token（平均约 89%），大幅延缓限额触发。
- **实用兼容**：直接模拟 OpenAI、Claude、Gemini 消息格式，支持 MCP（95 个工具）、A2A，21,000+ 测试保障稳定性。
- **零成本起步**：无需信用卡，11 个永久免费提供商，适合学生、个人开发者和低预算团队。

## 技术栈
- 语言：TypeScript
- 分发：npm 包、Docker 镜像、Electron 桌面应用
- 核心机制：OpenAI 兼容代理、多策略路由（17 种）、TLS 指纹伪装、电路熔断器
- 集成：MCP、A2A、多语言 i18n（42+ 语言）
- 许可证：MIT

## 核心能力
- **单端点多协议转换**：将请求翻译为 OpenAI、Claude、Gemini 等格式，任何客户端即插即用。
- **智能路由与回退**：订阅 → API → 廉价 → 免费四级自动切换，保障不间断运行。
- **Token 压缩**：RTK + Caveman 压缩会在请求前减少冗余文本（如 `git diff`、日志），大幅降低消耗。
- **丰富的提供商支持**：内置 231+ 提供商，包含 Yuanbao、Cloudflare Workers AI 等新成员，支持 cookie-session 认证。
- **多代理与 CLI 兼容**：直接搭配 Claude Code、Codex、Cline、Copilot 等 24+ 编码代理。
- **本地或自托管**：可本地运行，保护隐私；也提供 Docker 部署。

## 适用场景
- **个人开发者**：在 Claude Code/Cursor 中零成本使用多个大模型，避免每月付费。
- **小团队**：统一管理多工具的 AI 配额，防止单点限流导致开发中断。
- **受限地区访问**：通过 3 级代理和 TLS 指纹伪装绕过封锁。
- **Token 消耗敏感应用**：如自动化代码审查、CI 流水线中的大模型调用，利用压缩节省成本。

## 同类对比
与同类网关（如 LiteLLM、Portkey、One API）相比，差异点：
- **极致免费聚合**：专门扫描并维护大量无付费门槛的免费提供商，而非仅集成付费 API。
- **工具原生兼容**：内置对 Claude Code、Codex 等具体工具的 wire-image 支持（如 v3.8.45 的 agentrouter 动态适配）。
- **深度压缩**：独有的 RTK + Caveman 算法是其他网关未提供的。
- **全栈交付**：除 HTTP 网关外，还提供 CLI、MCP、A2A 和桌面应用，生态更完整。

## 版本动态
根据 v3.8.45 发布说明，近期更新包括：
- 新增 Yuanbao (腾讯元宝) 作为 cookie-session 提供商，支持 DeepSeek、Hunyuan 等模型。
- agentrouter 获得动态 Claude-Code wire image 支持，保证与 Claude Code 工具链身份认证兼容。
- Cloudflare Workers AI 批量密钥导入支持，修复账户 ID 隔离问题。
- 整体持续迭代，社区活跃（Discord、Telegram、WhatsApp）。
---

## ℹ️ 置信度与信息盲区

- 置信度：**medium**
- 信息盲区：README 截断，缺少最简示例和完整 provider 列表入口；未提供 RTK + Caveman 压缩的技术细节和白皮书链接；未说明桌面应用的安装方式及最低系统要求；缺少基准性能测试数据（吞吐量、延迟）；快速开始的具体 CLI 交互流程未展示