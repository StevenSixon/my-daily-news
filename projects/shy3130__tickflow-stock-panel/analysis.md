## 它是什么
一个自托管的A股量化工作台，提供选股、监控、回测功能，基于TickFlow数据，支持桌面客户端和Docker部署，面向个人散户和量化爱好者。

## 为什么火
- 开箱即用的桌面版，免去Python/Node环境配置。
- 内置20个策略，支持自定义信号和AI生成策略。
- 模块化设计，可接入Tushare等第三方数据，统一分析。
- 内置回测引擎（vectorbt或纯Polars）、监控中心与系统通知。
- 220星，持续迭代。

## 技术栈
- 后端：FastAPI, Pydantic, APScheduler, sse-starlette
- 数据层：Polars (向量化计算), DuckDB (查询), Parquet (存储), PyArrow
- 回测：vectorbt (全栈版), 纯Polars引擎 (桌面版)
- 前端：React 18, TypeScript, Vite, Tailwind CSS, Lightweight Charts, ECharts, Tanstack Query, Framer Motion, dnd-kit
- AI：可选OpenAI兼容接口
- 部署：Docker单容器，或Electron桌面客户端

## 核心能力
### 🔍 选股引擎
- 20个内置策略（趋势、形态、量价、涨停、反转、波动）
- 自定义信号系统：UI组合编译为Polars表达式，无需编码
- AI策略生成（需LLM Key）
- 策略商店统一管理

### 📊 指标流水线
- MA、EMA、MACD、RSI、KDJ、ATR、布林带、量比、原子信号等预计算，Polars向量化全A扫表，落盘enriched Parquet

### 🧪 回测
- 三种模式：个股、策略组合、自由信号组合
- 真实约束：T+1、手续费、滑点、止损、最大持仓天数
- 组合管理：最大持仓数、等权/自定义仓位
- SSE流式进度

### 📡 监控中心
- 四类监控：策略、个股信号、价格/涨跌、全市场异动
- AND/OR条件、冷却期、严重级别
- 实时SSE推送、系统通知、持久化触发记录

### 🔌 数据扩展
- TickFlow Free模式可体验10只票；付费解锁全A
- 支持Tushare等第三方数据源HTTP定时拉取、CSV/Excel上传、JSON写入
- 页面可视化配置扩展表，并入DuckDB查询面

### 🖥️ 桌面客户端
- Windows/macOS/Linux安装包，无需环境
- 数据存用户目录，卸载不丢失
- 纯Polars回测引擎可用，不含vectorbt

## 适用场景
- 散户建立量化选股、回测、监控流水线
- 量化爱好者统一管理策略和告警
- 自有数据整合分析
- 希望轻量级桌面工具替代重型客户端

## 同类对比
- vs 同花顺/通达信：专注量化分析，不内置交易，不自带数据
- vs QuantConnect/Backtrader：更轻量，自托管，桌面端可选，策略配置可视化
- vs zvt/VN.PY：部署更简单，聚焦快速扫描与监控

## 版本动态
当前v0.1.43 (2026-06-24)，提供Windows安装包，修复GBK编码崩溃、数据缓存、UI优化。路线图v2：Webhook下单、板块异动、早晚报。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供大规模回测性能基准（如全市场5000+股票回测耗时）；未说明TickFlow数据延迟及盘中实时行情支持情况（目前只看到盘后定时管道）；桌面版纯Polars回测引擎与vectorbt回测的功能差异细节未列出；扩展第三方数据时字段映射的具体示例和指南缺失