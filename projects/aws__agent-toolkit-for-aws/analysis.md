## 它是什么
AWS 官方发布的 Agent Toolkit，为 AI 编码代理（Claude Code、Codex、Cursor、Kiro 等）提供托管 MCP 服务器、技能包与插件，让代理能通过自然语言调用 300+ AWS 服务、执行 Python 脚本、搜索实时文档，并受企业级审核约束。

## 为什么火
AI 编码工具正快速演进，但让代理安全地操作云资源仍是难题。该工具包通过官方 MCP 端点统一鉴权、CloudTrail 审计和 IAM 代理条件键，既保留代理的操作自由度，又提供了人工操作不可比拟的可观测性和控制力。它兼容主流代理市场，降低上手门槛，迅速引起关注。

## 技术栈
- MCP 服务器：托管服务，通过 `mcp-proxy-for-aws` 代理访问
- 插件：针对 Claude Code、Codex、Cursor 的预配置包（含 MCP 设置和技能）
- 技能：基于 Markdown 的按需加载指令，跨代理复用
- 客户端工具：`uv` 运行 Python 代理，`npx` 安装技能
- 服务端：AWS 原生服务（CloudTrail、CloudWatch、IAM）提供企业控制

## 核心能力
- **全 AWS API 覆盖**：单一认证端点，覆盖 300+ 服务
- **沙箱化脚本执行**：代理可安全运行 Python 脚本进行复杂多步操作
- **实时文档检索**：无需认证即可搜索 AWS 文档和 API 参考
- **企业控制**：CloudWatch 指标、IAM 条件键区分代理与人工操作、CloudTrail 审计
- **多代理支持**：为 Claude Code、Codex、Cursor、Kiro 及自定义代理提供不同接入方式
- **领域技能**：aws-core（基础服务）、aws-agents（AI Agent 构建）、aws-data-analytics（数据湖/ETL）、aws-agents-for-devsecops（安全/运维）

## 适用场景
- 使用 Claude Code/Codex/Cursor 加速 AWS 应用开发与部署
- DevSecOps 团队让代理执行事件调查、代码审查、渗透测试
- 数据分析师通过 AI 代理构建 Glue/Athena 数据流水线
- 对代理操作有严格审计需求的企业云环境

## 同类对比
与 AWS Labs 早期开源的 MCP 服务器相比，本工具包增加了 IAM 代理条件键、CloudTrail 审计和经过端到端评估的技能，而非实验性组件。相比社区自建的 MCP 接口，官方支持带来更一致的 API 覆盖和长期维护承诺，但灵活性（如本地部署 MCP 服务器）可能受限。

## 版本动态
- 2026-04-23 仓库创建，2026-06-26 活跃推送
- 状态标记为 GA（正式可用）
- Star 数 1300+，生态增长迅速
- 插件版本受 Anthropic 官方市场管理，`mcp-proxy-for-aws` 建议固定 1.6.3 版
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供性能基准测试数据；未说明MCP服务器的具体实现语言和架构；插件内部技能指令的格式和细节未公开；未说明是否支持本地部署MCP服务器实例