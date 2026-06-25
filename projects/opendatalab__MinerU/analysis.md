## 它是什么
MinerU 是一个高性能文档解析引擎，将 PDF、DOCX、PPTX、XLSX、图片和网页等复杂文档转换为结构化的 Markdown 或 JSON，为 LLM、RAG 和 Agent 工作流提供清洁、可解析的数据。

## 为什么火
- 社区火爆：GitHub 69.4k stars，频繁更新，已被大量 LLM 应用集成。
- 精确解析：支持公式转 LaTeX、表格转 HTML、多栏布局、跨页表格合并，遵循人类阅读顺序，自动去除页眉页脚。
- 双引擎：VLM + OCR 双引擎，兼顾精度和效率，OCR 支持 109 种语言。
- 全面集成：提供 MCP Server 用于 AI 编程工具（Cursor/Claude Desktop 等），原生集成 LangChain、LlamaIndex、Dify 等 RAG 框架。
- 离线安全：支持完全离线部署，适配 10+ 国产 AI 芯片（昇腾、寒武纪等）。

## 技术栈
- 语言：Python（主要），也提供 Go/TypeScript SDK、REST API、Docker。
- 推理后端：`pipeline`（快速稳定，CPU/GPU 均可）、`vlm-engine`（高精度，可对接 vLLM/LMDeploy/mlx）、`hybrid-engine`（原生文本提取，低幻觉）。
- OCR 引擎：近期升级至 PP-OCRv6，准确率提升 11%，处理速度翻倍。
- 模型管理：自动选择下载源，缓存复用。

## 核心能力
- 多格式支持：PDF、DOCX、PPTX、XLSX、图片、网页。
- 结构化输出：Markdown、JSON，保留阅读顺序和语义结构。
- 公式/表格：LaTeX、HTML 忠实还原。
- 语言：109 种文字 OCR 识别。
- 处理优化：批处理、OCR 加速。

## 适用场景
- 构建 RAG 知识库（Dify、FastGPT 等集成）。
- 为 LLM 预处理训练数据（学术论文、报告）。
- 企业级文档数字化、离线敏感环境。
- AI 编程工具中直接读取文档内容（MCP 协议）。

## 同类对比
- 与 PyMuPDF、pdfplumber 相比：MinerU 更侧重 AI 就绪的结构化输出，而非纯提取。
- 与 Marker、Unstructured 相比：MinerU 提供更丰富的 Office 格式支持、双引擎选择、更好的中文/多语言支持和国产卡离线适配。
- 与商业化服务（如 Docling）相比：开源免费、可完全自托管。

## 版本动态
最新 3.4 版（2026-06-18）聚焦 pipeline 后端的 OCR 升级（PP-OCRv6），准确率提升约 11%，解析速度翻倍；优化模型下载体验，首次安装自动选源，支持缓存复用。
---

## ℹ️ 置信度与信息盲区

- 置信度：**medium**
- 信息盲区：README 未提供明确的安装指引和 CLI 示例，仅展示概览，quickstart 命令为推测；未提供全面 benchmark 数据（除 OmniDocBench 上的 OCR 指标提升 11% 外）；模型文件确切大小和下载机制未在 README 中说明；未说明系统依赖和硬件需求（如 GPU 显存）