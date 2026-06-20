## 它是什么
一套面向编码代理（Claude Code、Codex、Cursor 等）的“守卫技能”，在 AI 生成代码、测试或文档后立即执行专项审查，拦截系统性失败模式（如 hallucinated API、安全绕过、错误吞没等）。

## 为什么火
随着编码代理广泛使用，AI 产生的低级错误与不安全模式频繁流入代码库，传统检查工具难以捕获这些 LLM 特有缺陷。该项目以轻量技能包形式提供可组合的审查关口，安装即用、无外部依赖，迅速受到开发者关注。

## 技术栈
- 技能描述语言：Markdown + 轻量 YAML 元数据（agents/openai.yaml）
- 分发与运行：基于 [Skills CLI](https://github.com/vercel-labs/skills) 的 `npx skills add` 机制
- 无执行脚本、无网络调用、无 MCP 服务依赖，保证安全性
- 通过渐进式引用文件（references/）动态加载深度指南

## 核心能力
- **clean-code-guard**：检测 AI 常见代码异味（过度抽象、catch-all 错误处理、幻觉 API、命名不当、SOLID 违反等），基于 AI 特有模式研究
- **test-guard**：审查 AI 生成的测试，防止过度 mock、重复参数化、无效断言、实现细节绑定等
- **docs-guard**：比对文档与真实代码，验证 README、API 文档中的所有声明，消除符号幻觉与过时示例
- **wp-guard**：面向 WordPress 插件/主题/API，强制转义、权限检查、预处理语句、国际化、查询性能等安全规范
- **woo-guard**：在 wp-guard 基础上叠加 WooCommerce 特有规则，如 HPOS 兼容、订单元数据安全、结账校验、货币处理

## 适用场景
- 使用 AI 编码代理（如 Codex、Claude Code）生成 diff 后，在提交前进行自动或人工调用的审查
- WordPress/WooCommerce 开发者确保插件和扩展符合平台安全与性能最佳实践
- 团队 CI 中加入对 AI 生成代码的针对性质量阀

## 同类对比
- 与传统 linter（ESLint、PHPCS 等）相比，本工具专抓 LLM 产物缺陷，而非一般编码风格问题
- 与 WordPress/agent-skills（教学型技能）相比，本工具定位为“事后审查”而非“构建指导”，互补使用
- 其他审查关卡工具通常不区分来源，缺乏对 AI 生成模式的深度理解

## 版本动态
- 仓库于 2026-06-06 创建，次日推送，处于极早期但已获得 840+ 星标
- 当前仅包含 5 个技能，结构清晰，易于扩展
- 维护者使用本地校验工具确保技能质量，社区可通过 skills.sh 浏览和安装
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供各守卫的检测准确率、误报率或性能基准数据；依赖的 Skills CLI 具体版本未明确；未列出所有兼容代理及其确切版本支持范围；未说明除 WordPress/WooCommerce 外其他平台的特化守卫计划；缺少对守卫运行耗时或资源消耗的描述