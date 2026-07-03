## 它是什么
Page Agent 是一个运行在网页中的纯前端 JavaScript 库，注入后可直接通过自然语言指令控制网页界面——点击、填表、导航等。它不依赖浏览器扩展、后端服务、截图或多模态模型，只基于文本化的 DOM 信息与 LLM API 交互。

## 为什么火
Star 22k+，阿里开源，MIT 协议。直击 Web 自动化最大痛点：传统方案（Playwright、Puppeteer）需要无头浏览器或后端改造，Page Agent 让 SaaS 产品、内部系统一行 CDN 脚本就能获得 AI 操作能力，开发成本极低。

## 技术栈
- 语言：TypeScript
- 核心：解析网页生成文本 DOM 表示，调用 LLM（可 BYO），将 LLM 返回的动作指令映射为浏览器原生操作
- 灵感来源：browser-use（Python 生态）的 DOM 处理思路，但完全客户端化
- 可选扩展：Chrome 扩展（实现跨页面任务），MCP Server（Beta，允许外部 Agent 控制浏览器）

## 核心能力
- **极简集成**：一行 `<script>` 标签即可激活，Demo CDN 自带免费测试 LLM（仅限评估）
- **浏览器原生**：无需截图、无视觉模型、无跨域限制；所有操作在用户浏览环境中完成
- **LLM 无关**：支持任何 OpenAI-compatible API，默认推荐阿里 Qwen 系列，也可用其他
- **文本驱动自动化**：LLM 仅分析结构化 DOM 文本，不处理图像，降低延迟与算力需求
- **多页面与外部控制**：通过 Chrome 扩展串起多标签页任务；MCP Server 让外部 AI 控制浏览器

## 适用场景
- 为 SaaS 产品添加 AI Copilot，让用户用自然语言完成复杂操作
- 内部 ERP/CRM 中一句话完成多步表单填写，替代繁琐培训
- Web 无障碍：语音指令控制页面，辅助残障人士
- 构建跨页面的自动化工作流
- 为传统网站增加 AI 助手，无需后端重写

## 同类对比
- **vs browser-use**：browser-use 是 Python 服务端方案，需要无头浏览器与 Python 环境；Page Agent 定位为客户端 web enhancement，代码运行在用户浏览器里，无服务端负载。
- **vs Playwright AI**：Playwright 的 AI 能力依然依赖服务端或无头模式，集成复杂；Page Agent 对前端零侵入，更轻量。
- **vs 浏览器扩展类 Agent**：Page Agent 无需安装扩展即可运行，进一步降低分发门槛，同时提供可选扩展以支持高级能力。

## 版本动态
- 最新 v1.11.0（2026-07-03），活跃维护中
- 重构 LLM 请求修补逻辑，废弃 temperature 参数
- 新增对所有推荐模型的 CI 测试，保证模型兼容性
- 修复多窗口场景下错误的 active tab 问题
- 迁移图片资源到 page-agent.github.io，清理遗留动画代码
- 依赖项大量更新，保持现代生态对齐
- 维护者声明不接受纯 AI 生成的贡献，注重代码质量
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：无性能基准数据（如延迟、token 消耗、DOM 处理开销）；Free testing API 的速率限制、并发能力与生产可用性未说明；MCP Server 为 Beta 阶段，稳定性和功能完整度未知；对移动端浏览器的兼容性缺少明确声明；Awesome Page Agent 社区项目列表为空，尚无第三方应用案例