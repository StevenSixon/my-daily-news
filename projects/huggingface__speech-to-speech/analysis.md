## 它是什么
一个低延迟、全模块化的语音代理管道：VAD → STT → LLM → TTS，通过 OpenAI Realtime 兼容的 WebSocket API 暴露。每个组件都可热插拔，LLM 接口兼容 OpenAI 协议，可对接云端 API 或自托管的 vLLM/llama.cpp 服务器，实现完全本地、完全开源的语音交互栈。

## 为什么火
- **隐私与自主可控**：全部模型可本地部署，数据不出机器，适合敏感场景（家庭、医疗、企业内部助手）。
- **生产验证**：已作为对话后端在数千台“Reachy Mini”机器人上实际运行。
- **无缝替换**：从 OpenAI Realtime API 切换到自托管仅需修改连接地址，客户端零代码改动，如 Demo 所示。
- **低延迟流式架构**：组件多线程运行，流式转录、流式 LLM 生成、流式合成，支持中断和转折。

## 技术栈
- **语言**：Python 3.10+
- **核心库**：PyTorch, Transformers, Silero VAD, 多种 STT/TTS 后端（Parakeet, Whisper, Qwen3-TTS, Kokoro 等），MLX（苹果芯片）
- **LLM 接口**：OpenAI 兼容的 responses-api 或 chat-completions，也可直连 local Transformers/mlx-lm
- **通信**：WebSocket（OpenAI Realtime 协议 / 原始 PCM）、TCP Socket
- **依赖**：通过平台标记自动区分 macOS 和非 macOS 依赖，GGML/Qwen3-TTS 可选 CUDA 12.x 后端

## 核心能力
- **组件市场**：VAD（Silero）、STT（Parakeet/Whisper/Paraformer 等 6 种）、LLM（任意 OpenAI 兼容接口）、TTS（Qwen3/Kokoro/Pocket/MMS 等 5 种），通过 CLI 参数自由组合。
- **4 种运行模式**：realtime（OpenAI 协议，默认）、local（直接麦克风/扬声器交互）、websocket（原始 PCM）、socket（TCP 流，适合远程）。
- **实时特性**：实时转录、流式语音合成、VAD 断句、工具调用（LLM 支持 function calling）、推测性转折处理。
- **跨平台**：Linux/CUDA, macOS MPS/MLX, CPU 均覆盖，默认后端针对平台优化。

## 适用场景
- 构建智能音箱、陪伴机器人、AI 语音助手原型
- 企业自托管语音客服，避免数据泄露
- 研究语音交互低延迟管道及不同模型组合的对比平台
- 为任何 OpenAI Realtime 客户端提供本地替代后端

## 同类对比
| 方案 | 开源 | 本地部署 | 标准接口 | 模块化 | 流式低延迟 |
|------|------|----------|----------|--------|------------|
| OpenAI Realtime API | 否 | 否 | 是 | 否 | 低 |
| Speech-to-Speech (本项目) | 是 | 是 | 是（兼容 OpenAI） | 是 | 低 |
| Coqui TTS + STT 自行拼接 | 是 | 是 | 需自行开发 | 是 | 一般 |
| LiveKit + Deepgram 等 | 部分 | 部分 | 自定义 | 部分 | 低 |

优势在于“一个命令就能同时启动标准 API 和本地替代全部模型”，大幅降低集成与验证成本。

## 版本动态
- **最新版本** v0.2.10 (2026-06-11) 新增：并发会话池（`--num_pipelines`）、推测性转折修订、Paraformer 渐进式转录修复、Qwen3-TTS 语言别名规范化、工具调用响应完善等。
- 社区活跃，v0.2.10 已包含多名新贡献者。项目仍在快速迭代，组件支持不断扩充。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供具体延迟基准数值（如首音延迟、尾音延迟），仅描述“低延迟”；本地各模型内存/显存需求及推荐硬件配置未在 README 列出；多语言支持的详细能力（如 STT/TTS 语言列表、准确率）被截断，未完整展示；未见安全与隐私设计说明（如 WebSocket 鉴权、音频数据本地存储策略）；未说明与其他商业方案的性能对比测试