## 它是什么
LMCache 是一个独立的 KV 缓存管理守护进程，位于 LLM 推理引擎（如 vLLM）之下。它把 GPU 内存中的 KV 缓存透明地卸载到 CPU RAM、本地 SSD 或远程存储（Redis/S3 等），并支持跨请求、跨引擎实例甚至跨节点重用，相当于为 AI 原生知识提供了一个持久化、可插拔的缓存层。

## 为什么火
多轮对话、RAG 和 Agent 等长上下文工作负载中，重复的前缀计算会严重拖慢首 Token 延迟并浪费算力。LMCache 以引擎无关、故障隔离的方式系统性地解决了这一问题，已被 NVIDIA Dynamo 和多家云厂商集成，2024 年中开源至今 Star 近万，并加入 PyTorch 生态。

## 技术栈
- **语言**：Python  
- **推理框架**：深度集成 vLLM，同时支持 SGLang 等  
- **硬件**：CUDA / AMD ROCm / Moore Threads MUSA  
- **传输**：NIXL (RDMA)、NVLink、共享内存 (SHM)、TCP  
- **存储后端**：CPU RAM、本地 SSD、Redis/Valkey、Mooncake、InfiniStore、S3 兼容对象存储、NVIDIA CMX (DOCA)  
- **可观测性**：Kubernetes 风格指标 + KV 缓存专属命中率/生命周期统计  

## 核心能力
- **持久化分层缓存**：多级存储自动升降级，避免 GPU 内存溢出，同时缓存可在引擎崩溃后保留。
- **跨引擎共享**：独立守护进程使多个 vLLM 实例共享同一套 KV 缓存。
- **非前缀重用（CacheBlend）**：不仅限于前缀匹配，Prompt 任意位置的缓存块都可复用，并选择性重算以保证质量。
- **多进程/多节点架构（v0.4.7）**：支持跨进程协调、全局配额、共享内存传输，让大规模部署更易管理。
- **可插拔变换（SERDE）**：允许注入压缩、Token 丢弃等自定义策略。
- **PD 分离传输**：高效的 Prefill→Decode KV 搬运，支持 NVLink、RDMA 等高速通道。

## 适用场景
- 多轮对话、客服机器人：大幅减少重复前缀计算。
- RAG 长文档问答：文档嵌入可缓存复用。
- 多 Agent 协同系统：共享上下文缓存，减少重算。
- 高吞吐在线推理服务：通过缓存命中直接跳过 Prefill，降低延迟、释放 GPU 资源。

## 同类对比
- **vLLM 内建 prefix caching**：仅限单引擎进程生命周期，引擎重启即丢失；LMCache 提供外部持久化层，可跨引擎、跨节点共享。
- **Mooncake**：侧重于传输，LMCache 可将其作为传输后端插件使用，定位为更上层的缓存管理层。
- **FlexGen**：关注离线批量吞吐，LMCache 专为在线服务且注重可复用性。
- **NVIDIA KV Cache Manager**：多为硬件绑定方案；LMCache 强调供应商中立和多后端支持。

## 版本动态
v0.4.7（2026-06-13）引入了破坏性变更：重命名 `LMCacheGroupView`→`EngineGroupInfo`、`report_status` 改为 per-kernel-group，并废弃 `goblin`。新增 MP 协调器骨架、SHM 传输路径、混合内存分配器（支持 Qwen3.5 等 Mamba 模型）、NIXL DOCA MEMOS 与 Cloud Bigtable 后端，补齐了 CLI 配额管理命令。迁移时需参考 Release 说明调整配置字段。
---

## ℹ️ 置信度与信息盲区

- 置信度：**medium**
- 信息盲区：README 未提供 benchmark 或性能对比数据；快速开始部分缺少可直接复制运行的最小示例与配置；未列出官方已验证支持的模型列表；部署多进程模式的具体资源规格与依赖未说明