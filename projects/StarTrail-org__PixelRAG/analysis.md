## 它是什么
PixelRAG 不解析HTML，而是直接用无头浏览器把网页、PDF、图片渲染为截图瓦片，再用视觉嵌入模型（Qwen3-VL-Embedding 微调）检索图像，最终由多模态大模型从图像中读答案。项目提供开箱即用的 Wikipedia 8.28M 页面索引和 API，也支持自建索引。

## 为什么火
文本RAG丢掉表格、图表、布局等视觉线索，导致阅读理解失败。PixelRAG 保留完整视觉信号，让模型“像人一样看图”，在需要对比表格、看走势、读混排内容的场景优势明显。学术背景强（Berkeley SkyLab/BAIR/伯克利NLP），发布即带论文和基准索引，直接可复现。

## 技术栈
- 渲染：Playwright/CDP 截图瓦片（pixelshot 命令）
- 嵌入：Qwen3-VL-Embedding-2B，对网页截图数据做 LoRA 微调
- 索引：FAISS 向量检索
- 服务：FastAPI
- 训练：独立 uv 项目，Torch 2.9.1+cu129
- 插件：Claude Code 集成（pixelbrowse 技能）

## 核心能力
- 截图渲染：`pixelshot` 将任意URL或本地文档转为图像瓦片
- 视觉检索：用微调视觉嵌入直接搜图块
- 预建索引：828万Wikipedia页面索引已托管，无密钥API可用
- 自建索引：`pixelrag index` 一键从文档目录构建FAISS索引
- 多模态查询：支持文本和图像两种查询
- Claude 插件：`claude plugin install` 后通过 `/screenshot` 让Claude看图

## 适用场景
- 需要从复杂网页（表格、图表、多栏布局）提取答案的搜索/问答
- 文档视觉搜索（扫描件、报表、仪表盘截图）
- 给AI Agent提供“可视浏览”能力，避免纯文本丢失信息

## 同类对比
- 传统RAG框架（如LangChain文本块+嵌入）：丢失视觉结构
- 多模态RAG依赖OCR+文本：处理非结构化布局易出错
- 纯截图方案（如ScreenAI）：缺少端到端检索与大规模索引
PixelRAG 从截图→嵌入→检索→LLM读取完整串联，且提供了生产可用的渲染、嵌入和索引工具链。

## 版本动态
- 最新Chrome 150 CDP后端（2026-06-01），支持 rawFilePath 优化截图吞吐
- 文档中有吞吐优化指南，训练数据与模型已发布（LoRA权重、训练集）
- 数据整理与复现指南仍标为TBD，社区交流通道（Slack）活跃
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：README未提供检索精度benchmark（如Recall@K），论文可能包含但未截取；自建索引需多大内存/磁盘（Wikipedia索引约217GB，但自建无参考）；托管API的速率限制和稳定性无说明；PDF/图片渲染的具体能力边界未详述（README只提支持）；训练复现步骤部分标为TBD，实际可复现度未知