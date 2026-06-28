## 它是什么
Vibe-Trading 是一个开源的AI交易代理框架，通过一条命令即可赋予AI代理全面的交易能力。它集成了多市场数据源（A股/美股/港股）、LLM驱动的策略生成与回测、行情研究与信号执行，并提供Web UI和API。目标是让量化金融的开发与实验像聊天一样简单。

## 为什么火
- Star数两周内突破1.3万，社区高度活跃（大量PR和Issue）。
- 紧跟LLM与MCP协议趋势，将自然语言交互引入量化交易。
- 解决个人开发者数据获取分散、策略开发门槛高的问题，用“Vibe”理念降低实现成本。
- 支持从免费数据源到商业API的自动降级，兼顾可用性与成本。

## 技术栈
- 后端：Python 3.11+，FastAPI，Pydantic
- 前端：React 19，Web UI
- 数据：18个市场数据加载器（tushare、yfinance、akshare、东方财富等），多数据工具（资金流、龙虎榜、北向资金、SEC EDGAR等）
- 策略：LLM（OpenAI/Claude/DeepSeek等）驱动，回测引擎（支持假设→信号引擎→回测闭环），Research Autopilot
- 集成：MCP协议暴露只读数据工具，10个经纪商SDK连接器，可选本地数据缓存
- 部署：PyPI包，ClawHub，支持自托管，CSRF安全加固，API密钥认证

## 核心能力
- **一站式数据**：覆盖免费与付费源，自动切换，OHLCV清洗。
- **AI策略生成**：通过自然语言描述Hypothesis，Research Autopilot自动生成信号引擎和回测配置，执行归因分析。
- **Shadow Account**：从历史规则中提取交易信号，根据RSI等条件生成入场逻辑。
- **多代理协同**：支持事件驱动和Swarm运行，LLM容忍内容过滤。
- **安全与可观测**：CSRF防护，可选Shell工具，运行卡片，报告库。
- **社区生态**：Feishu/WeChat/Discord社群，快速迭代。

## 适用场景
- 个人量化研究员：快速验证交易想法，无需从头搭建数据管线。
- AI应用开发者：将交易能力集成到聊天机器人或自主代理中。
- 教育：学习和演示量化金融与AI的结合。

## 同类对比
- vs Backtrader/Zipline：Vibe-Trading更侧重AI原生交互，自动生成策略代码，而前者更依赖手动编写策略。
- vs QuantConnect：Vibe-Trading本地部署，数据源更灵活，且弱化云端依赖，隐私性更好。
- vs TradingView：提供Pine脚本，Vibe-Trading用Python+LLM，对程序员更友好，且可接入任意LLM。

## 版本动态
- v0.1.10：全球数据层18源+18工具，10经纪商连接器，Research Autopilot第一阶段，本地数据缓存，安全加固。
- 近期更新：修复OAuth超时、内容过滤崩溃、验证JSON严格化，增加Shadow Account条件入场、中文UI等。
- 路线图：持续扩展数据源和经纪商，深化Research Autopilot。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：无公开的实盘业绩或回测基准对比数据；经纪商连接器的实盘稳定性未量化；大量数据源的免费配额与限制未详细说明；LLM策略生成的过拟合风险未评估