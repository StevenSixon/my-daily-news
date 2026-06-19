## 它是什么
Headroom是一个上下文压缩层，在代理向LLM发送数据前压缩工具输出、日志、文件、RAG块和对话历史，减少60-95% token使用，同时保持相同答案。它提供库、代理服务器、MCP服务器和代理包装器，支持Claude Code、Cursor、Codex等主流编程代理。

## 为什么火
- 真实代理负载节省显著：代码搜索压缩92%，SRE调试压缩92%。
- 基准测试准确性无损失：GSM8K、TruthfulQA等性能不变，TruthfulQA甚至提升0.03。
- 零代码改动集成：代理包装器、MCP工具、drop-in代理服务器。
- 可逆压缩（CCR）：本地缓存原始内容，LLM可按需检索。
- 智能学习：`headroom learn`挖掘失败会话，写入建议至CLAUDE.md。
- 输出token缩减：修剪模型冗长输出，进一步降低成本。

## 技术栈
- 语言：Python（主）、TypeScript  
- 压缩算法：SmartCrusher（JSON）、CodeCompressor（AST）、Kompress-base（Hugging Face模型Kompress-v2-base）  
- 架构：CacheAligner（KV缓存命中优化）、ContentRouter（内容类型路由）、CCR（可逆存储）  
- 集成：FastAPI代理，支持LangChain、Vercel AI SDK、MCP  
- 平台：Anthropic、OpenAI、AWS Bedrock等  

## 核心能力
- 库调用：`compress(messages)`一行压缩  
- 代理服务器：`headroom proxy --port 8787`，任何语言可用  
- 代理包装：`headroom wrap claude/codex/cursor/aider/copilot`  
- MCP服务器：提供`headroom_compress`、`headroom_retrieve`、`headroom_stats`工具  
- 跨代理内存共享与自动去重  
- 输出token缩减：冗长度引导与努力路由减少模型输出浪费  
- 学习模块：根据历史会话学习最优压缩和冗长度  
- 可逆压缩：CCR存储原始数据，动态检索  

## 适用场景
- 编码代理（Claude Code、Cursor等）降低token成本  
- 大规模RAG压缩检索块  
- SRE/运维调试压缩大量日志  
- 多代理协作共享压缩内存  
- 任何需要优化LLM上下文窗口的应用  

## 同类对比
与其他prompt压缩库相比，Headroom提供多算法路由、可逆压缩和跨代理内存，并优化输出；与简单prompt缓存相比，CacheAligner主动调整前缀以提高KV缓存命中率，结合压缩效果更佳，且具备学习功能和仪表板监控。

## 版本动态
v0.26.0（2026-06-16）新增：Copilot BYOK包装器、仪表板代理统计、Mistral Vibe CLI支持、重读浪费归因、Bedrock跨区域压缩、前缀缓存面板净影响展示、对抗性输入鲁棒性评估网格、同工具重发检测、批量深度编辑优化等。社区活跃，持续迭代。