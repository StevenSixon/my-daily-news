## 它是什么
Craft Agents 是一个基于 Claude Agent SDK 与 Pi SDK 的开源桌面应用（Apache‑2.0），提供多会话管理、文档化工作流，并通过自然语言让代理自动发现并连接任何 API、MCP 服务、本地文件系统或数据库。它既是“代理原语”（agent‑native）的个人工作台，也可作为远程服务器供多个客户端接入。

## 为什么火
- **一句话连接万物**：告诉代理“添加 Linear 作为 source”，它会自动查找 API/MCP 文档、配置凭证，无需手写配置。
- **非 CLI 的代理体验**：桌面界面、会话状态管理、主题系统、权限模式，让不习惯命令行的团队也能高效使用。
- **多提供商与自托管**：支持 Anthropic、Google AI Studio、ChatGPT Plus、GitHub Copilot、OpenAI 等，并提供轻量级 headless 服务器和 CLI 客户端，适合个人与团队定制。
- **代理原语软件设计**：内置技能（Skills）、自动化、多文件 diff 视图、背景任务等，将代理能力深度融入日常工作。

## 技术栈
- **前端**：TypeScript、Electron、Bun
- **代理运行时**：Claude Agent SDK（v0.3.197）、Pi SDK
- **通信**：WebSocket（RPC）、TLS 加密
- **存储**：本地磁盘持久化会话历史
- **部署**：支持 Docker 容器化、macOS/Linux/Windows 安装脚本

## 核心能力
- **多会话收件箱**：会话状态流转（Todo→In Progress→Done）、标记、AI 自动命名
- **任意 API/MCP 集成**：内置 Google（Gmail、日历、Drive 等）、Slack、Microsoft REST API，MCP 标准服务器（Linear、GitHub、Notion 等），粘贴 OpenAPI 规范或截图即可连接
- **权限模式**：三级（探索/询问/自动）可随时切换，精细控制写操作
- **文件支持**：拖放图片、PDF、Office 文档，自动转换；多文件 diff 视图
- **技能与自动化**：自定义专业化指令，按标签、计划或工具调用触发代理会话
- **远程头模式**：headless 服务器 + 薄客户端，TLS 加密，适合 VPS 或持久化任务
- **CLI 工具**：可脚本化的终端客户端，支持连接、发送消息、运行集成测试

## 适用场景
- 个人生产力：用自然语言聚合 Slack、邮件、日历、文档等工具，让代理处理跨平台任务
- 技术团队：构建技能库、自动化重复操作（如 PR 审查、文档生成），并通过远程服务器共享代理工作区
- 快速原型：无需编写胶水代码，直接将新 API 或 MCP 服务接入对话，快速验证集成

## 同类对比
- **Claude Code / GitHub Copilot CLI**：纯命令行代理，侧重代码；Craft Agents 提供图形界面、文档视角和非代码任务的深度集成。
- **Open Interpreter**：本地自托管，风格类似 CLI；Craft Agents 强调跨服务连接与桌面体验，MCP 生态更标准化。
- **Continue / Cursor**：IDE 插件，聚焦代码生成；Craft Agents 更像通用工作台，不绑定编辑器。
- **开源优势**：Apache‑2.0 许可，允许自由修改和重分发，有 headless 与桌面双模式，同类闭源产品无法做到。

## 版本动态
- **v0.10.5（2026-07-01）**：正式支持 Claude Sonnet 5 模型（1M token 上下文、自适应思考），升级捆绑的 Claude Agent SDK 至 0.3.197，修复 Windows CLI 子进程控制台闪烁问题，API 无破坏性变更。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未说明 Pi SDK 的具体作用及与 Claude Agent SDK 的协同方式；未提供任何性能基准（令牌生成速度、内存占用、并发上限）；未明确桌面应用对各操作系统版本的详细兼容性列表（仅脚本推测支持 macOS/Linux/Windows）；未描述插件或扩展系统（除 Skills 外，是否有第三方市场）；未提及离线运行能力或数据隐私处理细节