## 它是什么
activity-frames 是一个 Python 库，为 AI 代理提供情景记忆（episodic memory）。它本地录制屏幕（通过配套的 nocta-recorder 引擎），将捕获的瞬间编译为结构化活动帧（activity frames），并通过 MCP 服务器将这些记忆提供给任意 AI 代理。核心亮点是完全本地、编译路径无 LLM，编译结果具有确定性且可溯源。

## 为什么火
- 解决 AI 代理痛点：大多数代理只有对话记忆，不知道用户今天做了什么，每次从零开始推理。activity-frames 提供真实活动记忆，让代理获得上下文。
- 极致成本节省：编译的常规任务（routines）可被计算机使用代理零 token 重放，避免了重复推理的开销，Routine Overhead Ratio 极低（详见 research/）。
- 隐私与确定性：所有处理在本地完成，编译引擎是纯确定性代码，无模型介入；证据可回溯到原始捕获行。
- 活跃社区：已被用于产品 Nocta，有学术论文，HackerNoon 热门故事，快速迭代（两周内从创建到 v0.2）。

## 技术栈
- 语言：Python
- 捕获引擎：默认使用 nocta-recorder（MIT 许可，预编译二进制，支持 Apple Silicon/Intel macOS、Linux x64），可替换。
- 存储：本地 SQLite（捕获数据库），编译器只读。
- MCP：标准 stdio 服务器，提供 5 个工具。
- OCR：设备端 OCR 读取屏幕文本。
- 实体解析：覆盖 25+ 网站（LinkedIn、GitHub、Google 服务等），未知站点降级为通用页面。

## 核心能力
- 屏幕录制（可开关音频），编译为 YAML/JSON/上下文块（“USER ACTIVITY”格式）。
- 两层级记忆契约：测量层（确定性）和推理层（需显式置信度标记）。
- 模式检测：重复点击、URL 循环、日常习惯，自动识别重复工作流。
- 通信视图（v0.2 新增）：提取邮件/消息窗口标题，不读正文，只报告存在。
- MCP 工具：get_context、get_activity、get_day_summary、get_patterns、get_communications。
- Python API：ActivityLog 类，轻松获取今日/任意日期活动。
- CLI：aframes record/context/today/patterns/mcp 等命令。
- 隐私：本地存储，不上传任何数据；文本内容需显式启用；音频默认关闭。

## 适用场景
- AI 代理日常上下文注入：在系统提示中嵌入用户今日活动，让代理知道用户做了什么。
- 计算机使用自动化（Computer Use）的成本优化：将重复操作编译为常规任务，代理直接重放，无需每次推理。
- 个人生产力分析：本地查看应用耗时、工作模式。
- 开发自己的代理记忆层：作为可嵌入的 Python 库集成。

## 同类对比
- 对话记忆（如 LangChain 的 ConversationBufferMemory）：仅记录对话历史，缺乏真实活动数据。
- Rewind / Granola：商业产品，功能类似但多依赖云端，且不提供零 token 的代理重放。
- 其他屏幕录制工具（如 Screenpipe）：捕获原始数据，但缺少编译为结构化帧、模式检测和 MCP 集成。
- 原生 computer-use 代理（如 OS-Copilot）：每一次任务都从屏幕截图推理，成本极高且不定确定性；activity-frames 提供预编译的确定性步骤。

## 版本动态
- v0.2.0（2026-07-16）：新增通信视图，MCP 工具从 4 增至 5，支持 `get_communications`，提供窗口标题级别信息；确定性编译确保双次运行字节级一致，通过 UTC/Tokyo/Auckland 时区测试；零新依赖。
- 短期目标：社区可扩展实体解析器，增强跨平台引擎稳定性。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供 routine overhead ratio 具体数值，需查阅 research/ 目录；Linux 和 Intel macOS 上的捕获引擎稳定性未经充分测试，可能存在未知问题；OCR 准确度未量化说明；Windows 支持状况未提及