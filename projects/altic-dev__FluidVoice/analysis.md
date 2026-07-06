## 它是什么
FluidVoice 是一款 macOS 原生的开源语音听写工具，主打全设备端语音识别（STT）与可选的本地 AI 增强（Fluid Intelligence）。它能在任何应用中实时将语音转为文字，支持快捷键全局触发，无需键盘。

## 为什么火
- **完全本地运行**：所有语音数据不离开设备，满足隐私需求。
- **多引擎支持**：内置 Parakeet、Nemotron、Cohere、Whisper 等多种声学模型，覆盖 40+ 语言，Intel 和 Apple Silicon 均可用。
- **智能增强**：本地 AI 可自动格式化、加标点、更正上下文，效果接近云端服务。
- **高活跃社区**：GitHub Star 近 6300，更新迭代快，已从 v1.5 快速演进至 v1.6.2。

## 技术栈
- **核心语言**：Swift（macOS 应用主体），Swift Package Manager 管理依赖。
- **AI 运行时**：Fluid Intelligence 为独立私有组件，疑似基于 llama-cpp 或类似本地推理框架，但细节未公开。
- **声学模型**：集成 NVIDIA Parakeet、Cohere Transcribe、Apple Speech、Whisper 等，部分模型经过 Native 优化实现极低延迟。
- **交互**：通过 macOS 辅助功能 API 直接键入任意应用，支持 notch 感知覆盖层。

## 核心能力
- **语音听写**：实时、低延迟，最新版 Parakeet 几乎零延迟。
- **命令模式**：语音控制 Mac 操作（启动 App、运行快捷指令等）。
- **写模式**：在任意文本框中听写或改写选中文字。
- **Fluid Intelligence**：本地 AI 进行智能格式化、上下文大小写修正、自定义词典学习、长文本处理（至 2000 词）。
- **标点符号直转**：口语标点（如“period”“dash”）直接转换为符号。
- **应用感知**：如 Slack/Discord 中的 @提及和 / 命令自动适配。
- **历史与统计**：可选本地录音保存、导出，每日用量统计。
- **高度可配**：所有功能均可选，覆盖层样式、模型选择、快捷键均可定制。

## 适用场景
- macOS 用户需要**隐私优先**的听写，不想将语音上传云端。
- 开发者、写作者需要**跨应用快速键入**，且希望本地 AI 辅助格式化。
- 多语言用户利用不同模型覆盖更多语种。
- 替代 Wispr Flow、Dragon 等商业软件，完全免费开源。

## 同类对比
- **Wispr Flow**：同样主打本地听写，但闭源，FluidVoice 开源且模型选择更多。
- **Apple Dictation**：系统内置，无需安装，但模型固定、增强能力弱，FluidVoice 在速度和准确率上更优（尤其是 Parakeet 引擎），且提供 AI 后处理。
- **Whisper Transcription**：桌面端 Whisper 工具通常只做转写，无实时键入和 AI 增强。

## 版本动态
- **v1.6.2（2026-07-06）**：自定义词典可通过语音学习修正；Fluid Intelligence 支持最长约 2000 词；增加应用感知 @mention；加入标点直转；多项性能与 UI 改进。
- **趋势**：本地 AI 能力持续增强，多平台计划（iOS / Windows / Linux 等待列表）表明未来将覆盖全设备。
- **社区反馈**：用户称 Fluid Intelligence 可能替代付费服务。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：Fluid Intelligence 的本地模型架构、训练数据和具体推理框架未公开；未提供与其他听写工具（如 Wispr Flow）在准确率、延迟等方面的定量对比；iOS/Windows/Linux 版本的具体发布时间未明确；对 Intel Mac 上 Parakeet 等模型的支持情况未详细说明