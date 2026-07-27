## 它是什么
`aisuite` 是 Andrew Ng 团队推出的 Python 库，为生成式 AI 提供两层抽象：统一的 Chat Completions API（屏蔽 OpenAI/Anthropic/Google 等差异）和 Agents API（支持函数工具、工具包、MCP 协议）。它也作为 OpenWorker 桌面 AI 助手的基础。

## 为什么火
- **Andrew Ng 品牌效应**：15402 Star，社区活跃。
- **极简多模型切换**：改一个 `model` 字符串即可替换供应商，告别各 SDK 学习成本。
- **原生 Agent 能力**：工具调用和自动多轮对话仅需几行代码，比 LangChain 更轻量直接。
- **桌面应用落地**：衍生的 OpenWorker 展示真实生产力场景。

## 技术栈
- Python 3.10+
- 各供应商原生 SDK（按需安装）
- 支持同步/异步、流式传输
- MCP 协议通过专用客户端集成
- 可插拔的状态存储（内存/文件/Postgres）

## 核心能力
1. **统一 Chat API**：`aisuite.Client().chat.completions.create` 封装所有供应商，支持 temperature、max_tokens、工具等通用参数。
2. **流式响应**：所有适配器提供一致的 OpenAI 格式 chunk。
3. **工具调用**：直接传递 Python 函数，库自动生成 JSON Schema 并执行调用，可选 `max_turns` 自动循环。
4. **Agents API**：声明式 Agent + Runner，内建文件、Git、Shell 工具包，支持工具审批策略和运行状态持久化。
5. **MCP 支持**：一行定义 MCP 服务器工具，支持过滤、前缀与连接复用。
6. **可扩展**：遵循 `<provider>_provider.py` 命名约定即可快速适配新供应商。

## 适用场景
- 需要快速对比不同 LLM 输出的研究或原型开发
- 构建需要工具调用（如查询天气、操作文件）的聊天机器人
- 自动化代码仓库分析、文档生成等 Agent 任务
- 作为自有应用的多模型基础层

## 同类对比
- **LangChain**：功能更杂，抽象层更重；aisuite 更聚焦于统一调用和基础 Agent。
- **LiteLLM**：类似统一接口思路，aisuite 额外提供 Agent 与 MCP 集成。
- **Haystack**：文档处理为导向，aisuite 偏重轻量模型交互。
- **OpenAI SDK**：仅限 OpenAI 生态，aisuite 覆盖多家。

## 版本动态
最新 v0.1.3（2026-07-20）新增 Nebius、DeepSeek、Cerebras、Inception Labs 等供应商，完善工具调用抽象（Part I/II），支持 reasoning content，开始 TypeScript 版本（aisuite-js），并增强 Token 计数和 CI 改进。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：缺乏与 LangChain 等框架的详细性能对比或 benchmark 数据；未说明大规模部署的连接池、速率限制与重试策略；未提及对 Embedding 模型或多模态输入的支持程度；TypeScript 版本尚处初始阶段，功能完整性未知