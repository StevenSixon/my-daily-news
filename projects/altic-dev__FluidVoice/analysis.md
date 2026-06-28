## 它是什么
FluidVoice 是一款 macOS 开源的离线语音转文字应用，完全本地运行，无需网络即可将语音实时转为文字并插入任意应用。核心卖点：极低延迟的本地推理、支持多种语音模型（从零下载的 Apple Speech 到高精度的 Nemotron / Whisper）、可选的本机 AI 增强（Fluid Intelligence）和云 AI 后处理。

## 为什么火
- **极致的隐私与速度**：所有语音处理均可留在本机，无数据泄露风险；同时自研的 Parakeet 实现号称“几乎零延迟”显示文字。
- **模型选择自由**：内置 8 种语音模型，覆盖 40+ 语言，从快速英文到多语言高精度，用户可自由切换，无需订阅。
- **实用的智能增强**：可选的本地 AI 修正能智能格式化、自动补全大小写，甚至通过语音控制 Mac（Command Mode）和重写文本（Write Mode）。
- **开源 + 活跃开发**：GPLv3 协议，社区反馈积极，迭代迅速，刚发布 v1.6.1。

## 技术栈
- 语言：Swift
- 平台：macOS 15.0+ (Apple Silicon 全模型支持，Intel 仅用 Whisper 模型)
- 推理引擎：内置自研的 Parakeet 运行时、Whisper、Apple Speech 框架等
- AI 增强：可选本地 Fluid Intelligence（闭源组件）或接入 OpenAI/Groq 等云 API
- 打包：Homebrew Cask、手动下载 DMG
- 测试/构建：Xcode、Swift Package Manager

## 核心能力
1. **实时语音转文字**：支持全局热键触发，菜单栏集成，会话历史保存在本地。
2. **多引擎选择**：可按需下载不同模型，适配低延迟英语场景或高精度多语种场景。
3. **AI 增强与自动化**：
   - Fluid Intelligence（本地）：智能格式化、上下文感知大写、后处理
   - Command Mode：用语音启动应用、执行快捷指令、控制系统
   - Write Mode：在任意文本框中口述写入或重写内容
4. **隐私与可定制**：所有功能均可选配，音频历史支持本地管理，不强制云服务；主题自适应；支持各应用独立配置。

## 适用场景
- 写作者、笔记党：快速将想法转文字，无需切换到键盘
- 隐私敏感者：会议记录、个人备忘，不希望上传到任何服务器
- 效率极客：利用 Command/Write 模式实现语音自动化
- 多语言用户：在一款应用中切换不同语言模型进行听写

## 同类对比
- **Apple Dictation**：系统自带，无需安装，但模型选择单一，无 AI 增强和灵活历史管理。
- **Otter.ai / Descript**：功能丰富但依赖云端，有隐私顾虑且需付费。
- **Speechify / Whisper 桌面版**： FluidVoice 的优势在于深度集成 macOS 无障碍 API、极快的本地 Parakeet 实现和可选的本地 AI 增强，且完全开源。

## 版本动态
- 最新稳定版 v1.6.1（2026-06-28）：改进自定义词典管理、快捷键冲突处理、模型下载安全校验、修复 UI 和 Ollama 流式请求等问题。
- v1.6.0 引入 Parakeet 极速重构、Fluid Intelligence 本地 AI、刷新主题和引导流程。
- 路线图中包含 MACOS_UI_AUTOMATION_BRANCH_PLAN.md，计划增强 macOS UI 自动化能力。
- 社区积极贡献，已有 4 位外部贡献者参与小版本修复。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供语音转写速度、延迟等 benchmark 数据；Fluid Intelligence 具体模型架构、算法细节未公开；Parakeet 自研实现的内部优化方式未说明