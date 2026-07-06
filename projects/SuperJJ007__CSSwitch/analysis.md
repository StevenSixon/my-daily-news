## 它是什么

CSSwitch 是一个运行在本地的模型切换器与启动器，专门给 Claude Science 使用。它把 Science 的推理请求转发到你自己的第三方 API（DeepSeek、通义千问、Kimi、MiniMax、GLM、OpenRouter 等），并用隔离环境生成临时启动门票，不侵入真实的 Claude 账号。桌面面板由 Tauri 2 构建，在 macOS 菜单栏一键切换模型配置。

## 为什么火

Claude Science 作为 Anthropic 推出的科研 Agent，功能强大但依赖付费订阅。很多研究人员、开发者想用自己已有的 API Key 或更便宜的国产模型，却受限于 Science 封闭的模型路由。CSSwitch 正好解决了这个痛点，并且把复杂的沙箱隔离、协议转换、Key 管理封装成一个简单桌面应用，降低了使用门槛。

## 技术栈

- **桌面端**：Tauri 2（Rust + Web 技术），macOS Apple Silicon 专用
- **代理**：当前使用 Python3 实现 HTTP 代理，计划迁移至纯 Rust
- **协议转换**：支持 Anthropic Messages ↔ OpenAI Chat Completions / Responses，流式响应通过非流式请求+本地 SSE 重放实现
- **隔离**：独立的 HOME、端口、数据目录，使用本地生成的启动门票，不读取真实 `~/.claude-science`
- **安全**：API Key 保存在 `~/.csswitch/config.json`（权限 0600），通过环境变量传递，代理仅监听 127.0.0.1 并使用路径 secret 校验

## 核心能力

- 面板管理数十套模型配置，一键设为当前并验证 Key
- 启动隔离的 Claude Science，模型选择器显示真实模型名
- 一键切回“官方 Claude”模式，保留原始订阅体验
- 支持 Anthropic 原生端点、OpenAI Chat/Responses 兼容端点、自定义中转站
- 自动移除上游请求的认证头，注入用户配置的第三方 Key
- 提供流式输出兼容（对 DashScope 等受限 provider 模拟流式）
- 所有数据和日志保存在本机，便于自查

## 适用场景

- 无 Anthropic 订阅但需要用 Claude Science 做文献分析、代码执行、论文写作的研究员
- 内网有私有模型部署，想通过自定义端点接入 Science 的团队
- 想对比不同模型在同一科研任务中表现的开发者
- 希望隔离账号、避免污染的测试/演示环境

## 同类对比

- **CC Switch**（为 Claude Code 设计的工具）：面向命令行，CSSwitch 更偏桌面科研场景，多了登录门票和沙箱隔离，且提供图形化配置面板。
- **官方 Claude Science**：模型锁定为 Claude，无法切换，且需付费订阅。
- **LiteLLM 等通用 API 网关**：功能更全，但需自行处理 Science 的认证逻辑、门票生成与沙箱隔离，CSSwitch 将这些复杂度封装为开箱即用的桌面应用。

## 版本动态

最新 v0.3.6（2026-07-06）新增 Custom OpenAI Responses 提供者，并改进了 DashScope 的工具调用兼容性（保守 tool-choice、移除不被接受的工具定义）。流式响应目前通过上游非流式请求+本地模拟 SSE 实现。代理仍依赖 Python3，后续将移入 Rust 单二进制。macOS 包尚未公证，首次启动需手动放行。当前不支持 Anthropic 托管的远程 MCP 服务，官网标注了已知限制。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供代理吞吐量、延迟等基准测试数据；Python代理的具体库依赖（如 httpx、fastapi）未在README中说明；应用UI尚未完成多语言，未给出具体计划；未说明与Claude官方订阅同时使用时的详细行为（如配置冲突检测）；未提供非macOS平台（Linux/Windows）的支持时间表