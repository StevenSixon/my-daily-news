## 它是什么
Superlog 是一个开源可观测 workspace，原生接入 OpenTelemetry 数据（Traces、Logs、Metrics），自动将噪音信号分组为事件，并提供可插拔的 AI 代理执行调查或修复。本仓库是社区版，包含 Web 控制台、API、OTLP 接入代理、后台工作器和默认的本地事件摘要代理。另有付费云版。

## 为什么火
- **YC P26 项目**：获得孵化器背书，社区关注度高
- **AI + 可观测性**：将大模型代理引入运维工具链，不止于可视化
- **自愈概念**：宣称“watch your infra while you sleep”，击中运维痛点
- **本地优先**：支持完全自托管，数据留在用户手中

## 技术栈
- **语言**：全栈 TypeScript
- **前端**：Vite + React (apps/web)
- **后端**：Node.js HTTP API (apps/api)，OTLP 代理 (apps/proxy)，后台 worker (apps/worker)
- **数据库**：PostgreSQL (Drizzle ORM 管理 schema)，ClickHouse 存储遥测查询
- **基础设施**：Docker Compose 一键启动

## 核心能力
1. **OTLP 原生接入**：通过 proxy 直接接收 OpenTelemetry 数据
2. **噪音分组**：利用指纹（fingerprint）技术将大量信号归并为事件
3. **AI 代理运行时**：可插拔的代理接口，社区版默认仅生成本地摘要；推测高级版可执行干预操作
4. **本地优先产品界面**：提供 Web UI 对分组后的事件进行排查
5. **开源社区版**：Apache 2.0 许可，无强制云依赖

## 适用场景
- 接到 OTLP 数据的自托管监控环境
- 团队不想维护复杂的告警规则，希望自动收敛噪音
- 探索 AI 代理在观测和自治运维中的应用
- 需要快速搭建开发/测试环境的小型项目

## 同类对比
- **Grafana + AI 插件**：Grafana 生态成熟但 AI 集成需额外配置，Superlog 将代理作为一等公民
- **Signoz**：同为 OpenTelemetry 原生，但缺少 AI 代理和自愈概念
- **Datadog/Honeycomb**：闭源商业产品，功能全但费用高，Superlog 提供开源自托管选项
- **Langfuse**：专注 LLM 可观测性，而 Superlog 面向通用遥测

## 版本动态
仓库创建于 2026-06-02，最新推送 2026-06-20，处于快速迭代早期；Star 数 902 反映一定社区兴趣。暂未见稳定版发布或路线图。
---

## ℹ️ 置信度与信息盲区

- 置信度：**medium**
- 信息盲区：AI 代理的具体修复能力未说明（社区版仅生成本地摘要）；无性能基准数据；事件分组算法未披露；ClickHouse 部署细节未提及；与同类工具详细功能对比缺失