## 它是什么
Orca 是一个面向开发者的 Agent 运行环境（ADE），允许在桌面和移动端同时管理、运行多个基于 CLI 的 AI 编码 Agent（如 Claude Code、Codex、Cursor 等）。每个 Agent 运行在独立的 git worktree 中，实现完全的上下文隔离，并支持并行执行同一任务后对比结果。

## 为什么火
- **并行多 Agent 对比**：可将同一 prompt 分发给多个 Agent，在不同 worktree 中生成方案，开发者像“评审委员会”一样挑选最佳结果。
- **任意 CLI Agent 兼容**：不局限于特定 Agent，所有遵循终端接口的编码助手均可接入，用户使用自有订阅。
- **移动端协同**：通过 iOS/Android 伴侣应用监控进度、接收完成通知并发送后续指令，随时掌控任务。
- **开发流程深度集成**：内置 GitHub/Linear 任务浏览、AI Diff 注释、浏览器设计模式、SSH 远程执行等，减少上下文切换。
- **社区活跃**：Star 过万，YC 背景，日更 Release，功能迭代极快。

## 技术栈
- **语言**：TypeScript，桌面应用（具体框架未明，推测为 Electron 或类似跨平台方案，因支持 Ghostty 终端、Chromium 内嵌浏览器等）。
- **终端引擎**：基于 WebGL 的 Ghostty 终端，支持无限分屏与持久化回滚。
- **Agent 集成**：通过 PTY 管理 CLI Agent 进程，并以 worktree 实现文件系统隔离。
- **移动端**：原生 iOS/Android 应用（iOS 已上架 App Store，Android 提供 APK）。
- **协议**：MIT 许可证，可能部分内置功能依赖后端服务（如自动化调度、用量跟踪）。

## 核心能力
- **并行 Worktree**：基于 git worktree 的隔离环境，每个 Agent 修改独立分支，避免冲突。
- **多 Agent 支持**：开箱即用支持 Claude Code、Codex、Cursor、OpenCode、Pi 等 20+ CLI 编码助手。
- **终端分割**：Ghostty 类终端，无限分屏，重启后保留会话。
- **设计模式**：内嵌 Chromium 窗口，点击 UI 元素即可将 HTML/CSS/截图发送给 Agent。
- **GitHub/Linear 原生集成**：在应用内浏览 Issues/PR，直接从任务启动 worktree 并审阅。
- **SSH 远程**：通过 SSH 在远程机器上运行 Agent，支持自动重连和端口转发。
- **AI Diff 注释**：在 diff 视图直接添加注释并反馈给 Agent 重新修改。
- **移动伴侣**：手机端查看 Agent 输出、发送后续 prompt、接收完成通知。
- **CLI 自动化**：提供 `orca worktree create` 等命令，可编写脚本驱动 Agent。
- **账户/用量管理**：可视化查看 Claude、Codex 等 API 用量和限流重置，热切换账户。

## 适用场景
- 需要同时对同一个问题从多个 AI 模型/Agent 获得方案并择优合并的开发者。
- 希望将多个 CLI Agent 统一管理，避免窗口切换和终端混乱。
- 远程服务器上运行重型 Agent，本地轻量监控。
- 自动化代码评审流水线：Agent 生成 PR，人工在 Orca 中注释后触发 Agent 修正。
- 在移动场景下跟进长任务（Agent 运行数小时，用户通过手机接收通知和发指令）。

## 同类对比
- **VS Code + Copilot/Cursor 插件**：单 Agent 模式，无原生多 Agent 并行和 worktree 隔离。
- **Shell 脚本 + tmux 多窗口**：可并行运行 CLI Agent，但缺乏统一 UI、文件对比、移动端监控、自动 worktree 管理。
- **LangChain/AutoGPT 类框架**：更偏向任务链构建，Orca 侧重于交互式开发环境，Agent 为第一公民。
- **其他 Agent IDE**（如 Open Interpreter）：功能更专一，未提供完整的 worktree 隔离、移动端、内嵌浏览器等一体化体验。

## 版本动态
- 最新 release v1.4.123（2026-07-05），每日活跃更新。
- 近期修复：跨 worktree 聊天泄露、Windows worktree 创建挂起、非阻塞 SSH 重连提示。
- 新增特性：Ghostty 主题导入、WSL Codex 运行时配置种子、无头服务模式自动调度启动。
- 持续优化：中文、西班牙语等多语言翻译，终端与浏览器快捷键行为调整。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未明确桌面端框架（Electron/Tauri），核心技术栈细节缺失；无性能基准数据（如并行 worktree 资源占用）；自托管/离线使用程度未说明，可能依赖云端账户或服务；CLI 工具具体安装方式与命令文档未在 README 展开；移动端确切技术栈与实现方式未透露