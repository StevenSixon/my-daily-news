## 它是什么

OpenClaude Improved 是一个开源的命令行编码代理，完全复刻了 Claude Code 的交互体验和工具链，但彻底解耦了对 Anthropic API 的依赖。你可以把它当作一个“万能适配层”，前端是熟悉的 Claus 式对话编程助手，后端可以任意接入 OpenAI、Ollama、Gemini、GitHub Models 甚至自建的 LiteLLM 网关。

项目由社区维护，从 Claude Code 源代码 fork 并改进，增加了 provider 配置、代理路由、gRPC 服务、VS Code 扩展等功能，但仍保持与上游的工具目录和命令格式兼容。

## 为什么火

尽管 Star 数只有 462，但仓库创建仅一天就吸引了关注（2026-07-26），反映出开发者对“非 Anthropic 不可”的反弹。它的核心卖点是“一次安装，随处运行”——你可以在公司内网用本地 Ollama 运行，也可以切换云端高性能模型，无需改一行代码。对成本敏感、要求数据本地化、或追求模型自由度的团队尤其有吸引力。

## 技术栈

- 运行环境：Node >=22，Bun 1.3.13+
- 语言：TypeScript
- 通信协议：HTTP（各 LLM API）、gRPC（headless 双向流）
- 集成：Ollama 原生聊天 API、Firecrawl 网页解析、VS Code 扩展
- 构建与测试：Bun 脚本，覆盖测试和 smoke test

## 核心能力

- **完整工具集**：bash 执行、文件读写编辑、grep/glob 搜索、子代理、MCP 协议
- **实时流式输出**：token 级流式，工具进度可见
- **多步推理环**：模型调用→结果反馈→再调用，支持深层流程
- **仓库地图**：基于 PageRank 的结构化地图，自动注入上下文
- **代理路由**：可为不同任务指定不同模型，支持内置代理（Explore、Plan、verification）
- **会话管理**：继续、恢复、分支，支持后台静默执行
- **视觉支持**：URL 和 base64 图像输入（取决于所选模型能力）
- **网络搜索**：默认 DuckDuckGo 免费搜索，可配 Firecrawl 引擎
- **gRPC 服务**：为 CI 或自定义 UI 提供 headless 双向流接口
- **VS Code 集成**：内嵌聊天、启动管理、控制中心

## 适用场景

- 需要在离线或内网环境使用编码代理的团队（搭配 Ollama 或本地 LLM）
- 想统一使用一个编码助手而不用切换多个后端 API 的公司
- 预算敏感，希望利用 OpenRouter 等低成本网关动态选择模型
- 希望拥有 Claude Code 体验但不想付费给 Anthropic 的个人开发者
- 在 CI/CD 流水线中通过 gRPC 自动化代码审查和修复

## 同类对比

与 Aider、Cline、Continue.dev、Cody 等竞品相比，OpenClaude 的差异点在于：
- **直接继承 Claude Code 功能完整性**：其他工具往往自己实现一套代理，而 OpenClaude 复用了 Anthropic 设计精良的 prompt 和工具交互模式，质量更接近原始体验。
- **模型无关的深度**：同样支持多后端，但 OpenClaude 对每个 provider 都有定制化的适配逻辑（如 Ollama 的原生 API 调用、最大上下文协商），不是简单的 OpenAI 兼容层转发。
- **VS Code 和 gRPC 双扩展**：同时满足交互式和 headless 场景，生态更完整。
- **缺点**：作为 fork 项目，可能跟不上上游功能演进；社区规模尚小，长期维护存疑。

## 版本动态

项目为全新发布（2026-07-26），正处于早期快速迭代阶段。目前没有发布 Tag 或版本号，所有功能集中在主分支。开发文档完善，贡献指南清晰，适合早期采用者尝鲜并参与建设。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：无性能基准对比数据（如与原生Claude Code或Aider的准确率/延迟比较）；未详细说明对非Anthropic模型时，提示缓存、扩展思考等特性的放弃或适配情况；缺少多语言代码生成质量评估；未提及大规模仓库下的工具调用失败率或上下文窗口管理策略的量化数据