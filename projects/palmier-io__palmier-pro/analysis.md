## 它是什么
Palmier Pro 是用 Swift 从零构建的开源 macOS 视频编辑器，内置生成式 AI（与 Seedance、Kling 等模型集成），并通过 MCP 协议暴露时间线控制接口，让 Claude Code、Codex、Cursor 等外部代理直接参与视频编辑项目。编辑器部分完全开源（GPLv3），生成式 AI 处理端闭源，需订阅。

## 为什么火
- **首个原生支持 MCP 的视频剪辑工具**：代理可通过 HTTP 发送命令操作轨道、剪辑、预览，相当于把视频编辑变成可编程任务。
- **YC S24 阵容 + 社区反馈**：9k Star 在 2 个多月内积累，说明需求明确。
- **工程师导向**：用熟悉的 LLM 工具链替代手动操作，降低视频制作门槛，尤其适合开发者快速产出 demo 或内容。

## 技术栈
- 语言：Swift（SwiftUI/AppKit）
- 平台：macOS 26 (Tahoe) on Apple Silicon 独占
- 通信协议：MCP over HTTP（本地 127.0.0.1:19789/mcp）
- 生成模型：Seedance、Kling、Nano Banana Pro（云端调用）
- 发行格式：DMG，通过 Sparkle appcast 更新

## 核心能力
- 完整视频时间线编辑（片段剪切、多轨排列、波纹删除、同步锁定等）
- 拖拽轨道重排序、Shift 拖拽执行波纹修整
- 内建生成式 AI 生图/生视频（需订阅）
- 本地 MCP 服务即时启动，暴露剪辑、项目控制等工具
- 与 Claude Code/Desktop、Cursor、Codex 原生集成，提供一键安装扩展
- 多语言 README，社区 Discord 活跃

## 适用场景
- 开发者批量生成或剪辑视频片段（自动化教程、产品演示）
- LLM 代理爱好者演练更具实操性的多步工具调用
- 小型团队快速出片，利用 AI 辅助初剪，减少重复劳动

## 同类对比
- **Adobe Premiere Pro / DaVinci Resolve**：功能完整但无 MCP 集成，AI 能力需插件，不开源。
- **CapCut/DavinCi Neural Engine**：封闭生态，无代理交互。
- **Flowblade/Kdenlive**：开源跨平台但非原生 macOS，无 MCP 设计。
Palmier 优势在于与 LLM 代理的原生结合，劣势是编辑功能成熟度尚不及老牌软件，且仅限于 macOS 26。

## 版本动态
最新 v0.4.5（2026-06-28）聚焦时间线增强：新增帧选取预览、波纹插入预览、轨道拖拽重排、波纹修整边缘拖拽等编辑功能，同时修复 MCP 数字参数溢出、窗口尺寸、fcpxml 格式等 bugs，并开始引入“Skills”设置页面，暗示代理能力可配置化。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未列出 MCP 工具集的具体命令/API 描述；生成式 AI 的模型选择及订阅价格未公开；未提供视频导出的格式、编码器支持细节；未说明是否依赖额外系统库（如 FFmpeg）；目前无性能基准测试或稳定性报告