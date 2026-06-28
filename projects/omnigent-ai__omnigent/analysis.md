## 它是什么
Omnigent 是一个开源的“元线束”（meta-harness），在 Claude Code、Codex、Cursor、OpenCode、Hermes、Pi 等 AI 编码代理之上提供统一编排层。你可以不重写逻辑就切换底层代理，强制实施策略和沙箱，并通过终端、浏览器、手机或桌面应用实时协作。

## 为什么火
随着多供应商的 AI 编码代理（Claude Code、Cursor、Codex 等）涌现，团队面临碎片化的治理、安全性和成本控制挑战。Omnigent 在 Star 5k+ 的验证下，成为解决这一问题的中心化框架，允许安全地混合使用不同代理、一键部署会话到云端沙箱，并实现团队共享会话。

## 技术栈
- 语言：Python 3.12+
- 安装方式：curl 脚本、uv、pip、Homebrew
- 依赖：Node.js 22+、npm、tmux（终端模式）、bubblewrap（Linux 沙箱）
- 模型接入：Anthropic/OpenAI API key、订阅凭证、兼容网关（OpenRouter、Ollama、LiteLLM 等）、Databricks
- 沙箱支持：Modal、Daytona、Islo、E2B、CoreWeave、Kubernetes、OpenShell、Boxlite、Databricks
- 部署：Docker、Render、Railway、Fly.io、Hugging Face Spaces、Modal、Cloudflare、Databricks Apps

## 核心能力
- **多代理编排**：通过统一的 YAML 配置或 SDK 接入 7 个以上代理，可在同一会话中调用不同代理
- **策略治理**：可设置批准流程、支出上限、工具限制，策略作用于服务器、代理或单次会话级别
- **沙箱隔离**：支持多种云端或本地沙箱，在隔离环境中执行代理
- **跨设备协作**：会话状态同步，支持共享、分叉、实时观看
- **原生终端 + Web UI + 桌面应用**：提供多种交互界面，桌面应用自动管理服务与运行器
- **模型灵活切换**：每个代理可独立绑定模型，会话中动态切换

## 适用场景
- 多团队共用一个代理运行时，需要统一的安全和费用管控
- 希望在不同 AI 编码工具间按任务做最优选择，避免重构
- 需要将代理执行环境部署到安全沙箱，防止越权操作
- 分布式团队通过手机或浏览器参与代理会话审阅

## 同类对比
- **AutoGen / CrewAI**：侧重于多代理对话与工作流，Omnigent 更侧重于对现有商业 CLI 代理的统一封装与沙箱执行
- **LangChain/LlamaIndex**：主要是 LLM 应用框架，不直接管理 Claude Code 等完整交互式代理
- **Aider / Continue**：单个编程助手，缺乏多代理治理和沙箱能力
- 优势：直接接入原生 CLI 代理（无 SDK 适配层）、丰富的策略与沙箱集成、首日即支持多供应商

## 版本动态
最新 v0.3.0（2026-06-27）加入 7 个新代理线束、原生桌面应用、项目分组、更多沙箱目标、Windows 基础支持、自定义代理创建 UI、并修复了多项稳定性问题。仓库活跃，社区通过 Discord 沟通。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供性能基准或与同类框架的量化对比；文档中未详细说明自定义 YAML 代理的完整规范，仅有 AGENT_YAML_SPEC.md 文件存在但内容未知；沙箱各目标的具体配置复杂度未详细展开