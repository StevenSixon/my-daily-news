## 它是什么
MARVIS-Agent 是一个本地优先的信用风险智能体，专为模型开发、验证、数据处理、特征工程与策略工作流设计。当前 V1.1.8 以模型验证为核心稳定工作流，能够执行 Notebook 验证任务，生成结构化证据并草拟 Excel/Word 报告。项目路线图规划 V2 增加代理插件/工具运行时，V3 建模、V4 策略等能力包。

## 为什么火
- **合规友好**：本地运行，模型与数据不出域，满足金融强监管要求，避免隐私泄露。
- **可审计**：通过 Notebook 运行时生成可复现的证据，便于内部审计与监管审查。
- **自托管免费**：MIT 协议开源，无需订阅费用，支持完全自定义品牌。
- **Agent 辅助**：自动对比历史验证指标（Agent Memory Foundation），提升效率。

## 技术栈
- **运行环境**：Python 3.11+，仅验证 macOS/Linux；Java 用于 pypmml（可选）。
- **后端**：FastAPI（提供静态 HTML/CSS/JS 服务）；Node.js 仅用于前端语法检查。
- **工作流**：Notebook 执行引擎，代理模式辅助报告生成。
- **本地存储**：基于 workspace 目录管理材料，支持多工作树与端口配置。

## 核心能力
- **笔记本验证运行时**：执行符合合同规范的 Jupyter Notebook，产出结构化指标。
- **历史记忆对比**：Agent Memory Foundation 记录并对比历史验证结果。
- **报告草拟**：支持自动生成 Excel/Word 验证报告。
- **品牌定制**：通过 workspace/branding/brand.json 覆盖名称、颜色、Logo。
- **更新工具**：内置 marvis update 命令实现 git 快速升级。

## 适用场景
- 信用风险模型开发与验证。
- 特征分析与特征工程。
- 策略生成、验证与监控。
- 模型治理与审计归档。
- 需要本地化处理的金融风控团队或咨询机构。

## 同类对比
README 未提供与其他工具的直接对比，但据定位可判断：
- 相比 SAS Model Manager、FICO Xpress 等商业套件，MARVIS-Agent 开源免费、本地部署，无供应商锁定。
- 对比纯代码库（如 scikit-learn + custom scripts），它提供标准化 Agent 辅助、报告生成和品牌管理，降低手工集成成本。
- 劣势：当前仅稳定支持模型验证，建模功能未完全实现，生态与成熟度较弱。

## 版本动态
- V1.1.8：首个稳定内置工作流（模型验证），Agent Memory Foundation 已落地。
- 路线图（docs/roadmap.md）：
  - V2：Agent Plugin/Tool Runtime，支持可扩展工具。
  - V3/V4：分别补充建模、策略能力包。
- 更新机制：marvis update 支持通过 git 快速合并最新代码，无需重建整个环境。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供与 SAS、ModelRisk 等商业信用风险工具的详细对比数据；未说明 V2、V3 等后续版本的具体发布时间；未包含 Notebook 验证的具体示例或默认工作流教程（仅描述合同规范）；未明确 Windows 原生安装（非 WSL2）是否支持；未说明 pypmml 所需的 Java 版本