## 它是什么
Omnigent 是一个开源的 AI agent 框架与“meta-harness”，为 Claude Code、Codex、Cursor、Pi 等主流编码 agent 提供统一编排层。你可以用 YAML 定义自定义 agent，并在同一个会话中调度、监督、切换他们，无需重写任何 harness。同时提供策略引擎、沙箱隔离、多设备实时协作和云端部署能力。

## 为什么火
发布不到 10 天即获近 4000 star，因为它切中了开发者实际痛点：不同 AI 编码助手各有所长，但单独使用容易割裂。Omnigent 允许同一个会话中混合多个 agent，让 Claude 写代码、Codex 审查，或将任务分发给不同特化的子 agent，同时为所有操作施加统一的安全策略和沙箱。对团队而言，它带来了前所未有的控制力与灵活性。

## 技术栈
- 语言：Python 3.12+，CLI 工具 `omnigent`（缩写 `omni`）
- 依赖：Node.js 22+（用于 Claude/Codex/Pi 的 harness），tmux，Linux 需 bubblewrap 做 OS 级沙箱，macOS 使用内置 seatbelt
- 部署支持：本地 `docker compose up`，一键部署到 Render、Fly.io、Railway、Hugging Face Spaces、Modal 等云平台
- 模型接入：第一方 API 密钥、OpenAI/Anthropic 订阅、兼容网关（OpenRouter/Ollama/vLLM）、Databricks
- 沙箱后端：Modal、Daytona、Islo、NVIDIA OpenShell、E2B、CoreWeave、Podman 等

## 核心能力
- **多 agent 编排**：同一会话启动 Claude Code、Codex、Cursor、Pi 及自定义 agent，支持 agent 间相互 review，子代理在独立 git worktree 中并行工作
- **统一策略治理**：服务器/agent/会话三级策略，可暂停等待审批、限制支出、工具白名单，发送通知
- **沙箱隔离**：所有 agent 运行在沙箱中，通过 `credential_proxy` 注入认证信息，密钥不进入沙箱
- **多设备实时协作**：终端、浏览器、手机同步会话；可分享会话给队友实时观看或共同操作，支持 fork 会话
- **灵活模型切换**：在会话中用 `/model` 切换模型，支持多种凭证类型，默认值可按 agent 独立设置
- **一键自升级**：`omni upgrade` 自动检测安装方式并升级，支持索引 URL 配置
- **扩展性**：用 YAML 定义 agent，SDK 插件化接入新 harness（v0.2.0 新增）

## 适用场景
- 研发团队同时使用多种 AI 编码助手，需要统一入口、相互审查和策略管控
- 需要强安全约束的企业环境（禁止某 agent 联网、限制命令执行等）
- 远程/分布式团队，需要实时共享和协作 AI 编码会话
- 个人开发者希望在手机端继续电脑上的 agent 会话

## 同类对比
相较单一 Agent（如 GitHub Copilot、Claude Code 单独使用），Omnigent 提供了编排与审查能力。对比 LangChain、AutoGPT 等通用 agent 框架，它更聚焦于编码场景，且对现有 CLI agent 做到“无痛集成”，无需重写逻辑。与其它多 agent 编排项目相比，其核心差异在于原生集成多个头部编码 agent、内置策略和沙箱、直接从移动端操控的生产力设计。

## 版本动态
当前版本 v0.2.0（2026-06-19），刚刚在一周前发布。新增多厂商 agent SDK、更多沙箱与部署目标、secretless egress、MLflow 追踪、`omni upgrade` 命令等大量功能，并修复了数个关键 bug。项目尚处 alpha 阶段，但迭代速度极快，社区贡献活跃。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：无性能基准测试数据（如编排延迟、多 agent 并发开销）；策略系统的完整表达能力未提供详尽说明，仅靠文档推断；对 Cursor 集成是否支持全部 Cursor 功能或存在限制未明确；无大规模部署案例或生产环境稳定性报告；沙箱各后端的成熟度和隔离强度无量化比较