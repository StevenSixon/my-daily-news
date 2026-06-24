## 它是什么
AutoCVE 是一个 Agent 驱动的自动化 CVE 发现平台，专注于源码审计、漏洞验证与报告生成。它通过编排 Recon、Scan、Triage、Finding、Verification 等多个 LLM Agent，实现从项目导入到 CVE 报告全流程自动化。

## 为什么火
- **实打实的漏洞产出**：在 7 天测试中挖掘出 30 个真实 CVE，涵盖 14 个开源项目，最高 CVSS 9.9。
- **面向 CVE 的低门槛工具**：一行命令部署，提供 Web 界面，降低了自动化漏洞赏金的技术门槛。
- **LLM 驱动的深度审计**：不同于传统 SAST，它利用 Agent 的 ReAct 循环与上下文理解，能发现逻辑漏洞、授权缺陷等深层问题。

## 技术栈
- 后端：Python 3.11+、FastAPI、PostgreSQL
- 前端：React 18
- Agent 框架：基于 ReAct 循环的 Multi-Agent 编排
- 部署：Docker Compose、预置前端/后端容器镜像
- 许可：AGPL-3.0

## 核心能力
- **一键 CVE 挖掘流水线**：筛选项目 → 导入仓库 → 创建审计任务 → Agent 审计 → 生成报告，人只需提交报告即可申请 CVE。
- **Multi-Agent 协同审计**：Orchestrator 调度 Recon（信息收集）、Scan（工具扫描）、Triage（误报过滤）、Finding（深度挖掘）、Verification（动态验证）五个专用 Agent。
- **三种审计模式**：增强扫描（快速扫+过滤）、智能审计（仅 Finding Agent 深挖）、综合审计（全流程覆盖）。
- **Finding Agent 核心设计**：内建 ReAct loop、专项工具调用、nudge 纠偏与 FinalizeFinding 终止机制，确保产出可申报 CVE 的高价值漏洞。
- **交互式审计**：用户可随时追问 Agent，补充证据、复现步骤或扩展分析，审计过程可视化追踪。
- **漏洞管理**：Agent 自动去重、结构化入库，支持中文/英文/CVE 多种报告导出。

## 适用场景
- 安全研究员与漏洞赏金猎人快速审计开源项目，批量发现 CVE 级漏洞。
- 企业安全团队对内部代码库或第三方依赖进行自动化审计。
- 渗透测试团队辅助信息收集与深度漏洞挖掘。
- 学习 Multi-Agent 安全审计架构的参考实现。

## 同类对比
- **vs. Semgrep/CodeQL**：传统 SAST 依赖静态规则，难以覆盖逻辑漏洞；AutoCVE 通过 LLM 推理可发现越权、SSRF 等复杂场景。
- **vs. 一般 LLM 审计脚本**：多数方案仅简单调用 API，缺乏 Agent 编排与中断纠正能力；AutoCVE 提供完整的 ReAct 状态机与工具链。
- **局限**：需自行配置 LLM 后端，AGPL 许可可能影响商用二次开发。

## 版本动态
- v1.0.0 于 2026-06-15 发布，为首次正式版本。
- 新增 Agent 直审功能、优化 ReAct 循环逻辑、修复用户对话不走 ReAct loop 的 bug。
- 引入漏洞管理系统、Skills 扩展，文档与部署镜像同步完善。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：README 未说明支持的 LLM 模型列表及其配置方式，需进入 Web 界面或查阅 docs/ 才知晓；未提供各 Agent 审计单个项目的时间、资源消耗基准数据或推荐硬件配置；CVE 成果的具体复现步骤与审计过程在 README 中未展开，细节收录在外部仓库（larlarua/vulnerability-reports）