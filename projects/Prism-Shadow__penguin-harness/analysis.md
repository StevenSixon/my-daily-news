## 它是什么
PenguinHarness 是一个运行在桌面的自动化Agent工厂，连接1000+模型，能够用一句自然语言指令生成完整的AI应用（如RAG、数据分析工具），并通过内置的Skills机制让Agent自我评估与优化，实现“Agent构建Agent”的闭环。

## 为什么火
开发者厌倦了手动编写Agent应用和昂贵的闭源方案。PenguinHarness将构建成本压到极低——用DeepSeek V4 Pro生成一个带引用链接的RAG应用仅消耗2美分，数据分析精度达到最佳且成本为Claude Code的1/70。更诱人的是，它把Agent创建和持续改进的流程都自动化了。

## 技术栈
- **语言&运行时**：TypeScript，Node ≥24（安装包内置运行环境）
- **架构**：monorepo，分为 penguin-core、penguin-server、penguin-cli、penguin-web 等包
- **接口**：CLI、SDK（@prismshadow/penguin-core）、Web UI（端口7364）
- **模型支持**：DeepSeek V4、Kimi K3、GLM 5.2、GPT 5.6、Claude 5 等，以及任何OpenAI协议端点

## 核心能力
- **Goal Mode**：设定目标与token预算，系统持续驱动任务直到完成或耗尽预算，并写入GOAL.yaml协议
- **低层高效工具集**：减少无谓的tool call，针对开源模型深度优化，token消耗远低于LangChain等框架
- **内置Skills**：办公（数据分析、网页抓取）、软件开发（Web设计、软件工程）、AI应用开发（penguin-sdk、vllm、ollama）、Agent调优（创建、评估、优化）
- **自进化循环**：运行benchmark → 找出失分点 → Agent自我优化 → 生成新版本，所有变更可追溯
- **跨平台**：Linux、macOS、Windows 10+，统一安装脚本

## 适用场景
- **极速原型**：一句话生成带检索的问答系统、自动化报告工具
- **数据分析**：以几美分的成本完成复杂数据任务
- **Agent研究**：快速搭建评估环境，验证不同模型与prompt策略
- **自动化工作流**：通过CLI/SDK嵌入现有流程，让Agent自动编写脚本、调度任务

## 同类对比
| 特性 | PenguinHarness | LangChain | Claude Code / Codex CLI |
|------|---------------|-----------|------------------------|
| 构建方式 | Agent自动生成完整应用 | 手工组合chain | 手工编写代码 |
| 成本(数据分析) | 极低（1/70 Claude Code） | 中等（二次模型调用） | 高 |
| 自我优化 | 原生支持Skills自进化 | 需额外开发 | 无内置机制 |
| 开放性 | 开源，本地运行，任何模型 | 开源，本地可选 | 闭源/特定模型 |

## 版本动态
- 2026-07-19 创建，截至7-27 获得202 star
- v0.1.4 修复npm发布问题，使v0.1.3功能（Windows支持、Goal模式、子agent面板、LLM错误恢复）全量上线
- 路线图包含：公开Benchmark套件、桌面应用、Agent模板市场、公司级自进化、带权限治理的Shell集成
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：benchmark 具体数值和测试方法未公开，仅提供图示对比；多会话并发模型调用的限制未说明；团队/多用户支持和权限管理细节未披露（仅提及默认登录和Roadmap中的OpenShell）；自我优化 Skills 的稳定性与安全边界未量化描述