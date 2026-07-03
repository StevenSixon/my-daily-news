## 它是什么

`chrome-devtools-mcp` 是一个Model Context Protocol (MCP) 服务器，让任何支持MCP的AI编码代理（如Claude、Cursor、Copilot）直接控制并检查运行中的Chrome浏览器。它暴露了Chrome DevTools的全部能力，包括网络请求分析、控制台检查、截图、性能录制，并利用Puppeteer实现稳定的浏览器自动化。同时提供独立的CLI工具，无需MCP也可使用。

## 为什么火

- **AI代理的浏览器渴求**：现代编码助手需要与真实前端环境交互，本项目将最权威的浏览器调试工具深度注入AI工作流，成为代理化开发的关键基础设施。
- **官方维护与高社区认可**：由Google Chrome DevTools团队直接维护，Star数超过45k，已被Antigravity、Claude Code、Cursor等多个主流AI客户端官方集成。
- **专业性能分析能力**：超越普通的点击/截图自动化，直接集成Chrome DevTools的Trace录制、核心Web指标（CrUX数据）、堆快照对比等高级功能，为AI代理提供可操作的性能优化洞察。

## 技术栈

- 核心语言：TypeScript
- 浏览器操控：Puppeteer（利用Chrome DevTools Protocol）
- 协议层：MCP (Model Context Protocol)，支持标准输入输出和Streamable HTTP传输
- 运行依赖：Node.js LTS版本、Chrome稳定版或Chrome for Testing
- 分发方式：npm包 `chrome-devtools-mcp`，推荐使用 `npx` 快速启动

## 核心能力

- **深度浏览器调试**：检查网络请求与响应、查看控制台消息（含源码映射堆栈）、捕获全页面或元素截图、查看HTML结构。
- **性能分析套件**：记录性能Trace，解析核心Web指标（LCP、INP等），可获取Chrome用户体验报告（CrUX）的基准数据。
- **高级自动化**：Puppeteer驱动的点击、输入、导航等操作，自动等待结果，比简单的脚本更可靠。
- **内存分析（v1.5.0新增）**：获取堆快照中的重复字符串，支持堆快照比较，利于发现内存泄漏。
- **灵活运行模式**：提供完整工具集与`slim`模式（仅基础浏览器操作，适合简单任务），支持无头模式。
- **多平台集成**：提供对数十种AI客户端（Antigravity、Claude Code、Copilot、Cursor、Gemini CLI等）的详细配置指南，部分客户端还提供skill插件以增强代理的使用效率。

## 适用场景

1. **AI辅助前端调试与优化**：开发者用AI代理直接操作浏览器，诊断性能瓶颈、网络问题、控制台错误，并获取改进建议。
2. **自动化端到端测试**：在CI/CD中集成Chrome，让AI代理生成并执行测试，捕获快照与性能数据。
3. **网页自动化脚本生成**：通过对话形式让AI编写并验证浏览器自动化流程（如表单填充、数据抓取）。
4. **代理驱动的应用监控**：实时检查线上页面的行为、性能，并由AI给出分析报告。

## 同类对比

- **Puppeteer/Playwright 本身的 MCP 封装**：社区存在其他类似项目，但 `chrome-devtools-mcp` 的独特价值在于**直接暴露DevTools的性能与内存分析工具**，而不只是页面操作。其团队背景确保了与Chrome协议同步更新。
- **Browserbase 等云端浏览器工具**：可结合使用，但本工具更轻量，本地Chrome即可满足，且数据不出本机（除非使用CrUX服务）。
- **官方DevTools本身**：专为人类操作设计，`chrome-devtools-mcp` 将其结构化为AI可调用的工具，打破人与代理之间的界面鸿沟。

## 版本动态

最新 v1.5.0（2026-07-03）聚焦内存分析与安全性：
- 新增 `get_heapsnapshot_duplicate_strings` 工具及堆快照对比功能，强化内存泄漏检测。
- 修复CLI错误消息以更好引导AI代理；PID目录使用安全权限（0o700）。
- 增强扩展强制输出路径校验，完善allow/block列表在 `loadResource` 中的处理。
- 文档优化，如修复Antigravity配置示例。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供与其他浏览器MCP工具的性能对比基准数据；未明确说明支持的具体Chrome最低版本或Edge等Chromium浏览器的兼容性细节；未描述在多浏览标签页或多浏览器实例并发场景下的稳定性与资源开销