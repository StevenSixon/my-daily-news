## 它是什么
`google/agents-cli` 是一套面向**编码助手**（如 Claude Code、Codex 等）的命令行工具与技能包，让 AI 编码助理精通在 Google Cloud 上构建、评估和部署企业级 AI 代理。它本身不是编码代理，而是“教”编码代理怎么用 ADK 和云服务的教练。

## 为什么火
随着 AI 编码助手流行，开发者想让助手直接生成可落地的 Agent，但助手缺乏 Google Cloud 具体知识。agents-cli 以可安装的“技能包”为编码助手注入领域知识，同时提供标准化 CLI，填补从代码到生产的天堑。Star 数短时间内突破 4k，背后有 Google 官方背书。

## 技术栈
- 语言：Python
- 包管理：uv
- 运行依赖：Node.js（部分技能安装）
- 核心框架：Agent Development Kit (ADK)
- 云服务：Google Cloud（Agent Runtime、Cloud Run、GKE、Gemini Enterprise）
- 模型：Gemini（可通过 AI Studio API 在本地运行）

## 核心能力
1. **脚手架**：一键生成标准 Agent 项目，支持增强部署、CI/CD、RAG 等模板。
2. **评估**：内置评估数据集生成、自动打分、失败模式分析、提示词优化。
3. **部署**：一条命令部署到 Cloud Run、GKE 或 Agent Runtime。
4. **发布**：注册到 Gemini Enterprise，启用原生调用。
5. **可观测性**：集成 Cloud Trace、日志与第三方监控。
6. **技能注入**：提供 7 个结构化技能文件，编码助手加载后即可指导用户完成全流程。

## 适用场景
- 团队使用 Claude Code / Antigravity / Codex 等编码助手开发 AI Agent，需快速接入 Google Cloud 生态。
- 已有 ADK 项目，想通过助手实现自动化评估与部署。
- 独立开发者希望通过标准化流程缩短从概念到上线的时间。

## 同类对比
- **直接使用 ADK**：ADK 是底层框架，agents-cli 提供了面向编码助手的“驾驶指南”和经过验证的模板，降低学习曲线。
- **LangChain/其他框架**：侧重生成本身逻辑；agents-cli 专精 Google Cloud 的生产部署与运营。
- **其他 CLI 工具**：通常面向人类操作，agents-cli 独特之处在于技能包是为 AI 编码代理设计的，使“AI 教 AI”成为可能。

## 版本动态
最新 v0.6.1（2026-06-28）重点修复：
- `publish gemini-enterprise` 默认改为 ADK 注册，更可靠；修复 A2A 重复注册和 URL 错误。
- `update` 命令失败时正确报告错误，不再虚假显示成功。
- 所有模板项目的依赖 google-adk 升级至 2.3.0。表明项目处于活跃迭代中，但仍在“预览”阶段。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：技能文件的具体格式（是否为 Markdown 指引）未公开；未提供与直接使用 ADK 的性能或效率对比数据；部署到 Cloud Run/GKE 的默认资源配置和成本未说明