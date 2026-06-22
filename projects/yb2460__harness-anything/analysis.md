## 它是什么
一个针对Windows平台的AI Agent控制中枢（harness），通过COM自动化接口将WPS/Microsoft Office、Zotero、Adobe Illustrator、Adobe Photoshop等桌面软件封装为统一的CLI命令，供AI Agent或脚本直接调用。包含47个办公命令、27个学术研究Skill，以及矢量/位图设计操控能力。

## 为什么火
满足“让LLM操作真实软件”的硬需求：多数AI集成仅靠API或模拟输入，本项目通过成熟的COM接口直接驱动本地应用，可靠性和功能完整性更高。集办公、学术、设计于一体，一次性解决多个场景的Agent工具需求，且以MIT协议开源，Star增长迅速。

## 技术栈
- 语言：Python 3.10+
- 核心依赖：pywin32（COM桥接）、Click（CLI框架）
- 操控目标：WPS Office 2019+ 或 MS Office 2016+、Zotero 7+、Adobe Illustrator 2023+、Adobe Photoshop 2023+
- 运行环境：Windows 10/11

## 核心能力
- **WPS/Office操控**：Writer/Calc/Impress全功能操作，包括段落、表格、图表、公式、导出为DOCX/PDF/PPTX等，内置4套PPT设计预设和14种布局，支持质量审查。
- **Zotero学术智能体**：27个Skill覆盖文献检索、写作、审稿、可视化、分析及完整学术流水线。
- **Illustrator操控**：新建文档、图层管理、矢量图形绘制（矩形/椭圆/线条/多边形）、文字添加与样式、导出为SVG/PNG/PDF等。
- **Photoshop操控**：PSD项目操作、图层/选区/图像调整、文字图层、滤镜、导出为PNG/JPEG/WebP/PSD。
- **数据驱动PPT生成**：JSON数据输入，13种元素类型自动路由，生成多页高质量演示文稿（附5校招生数据案例）。

## 适用场景
- AI Agent需要直接操作Office文档生成报告、演示文稿
- 学术研究人员快速完成文献综述、系统评价、期刊图表制作
- 自动化设计流水线：LOGO生成、海报批量制作、图像处理
- 教育或招生场景下的数据报告自动PPT输出

## 同类对比
与纯API方案（如通过OpenAI生成Office文档）相比，本项目直接操控本地软件，效果更可控、排版更精确；与UiPath等RPA工具相比，定位更垂直、更轻量，专为Agent设计。与单一软件操控库（如python-pptx）相比，统一CLI且覆盖软件更多，但受COM依赖限制，仅Windows可用。

## 版本动态
- 项目创建于2026-05-27，最新推送2026-06-12，处于活跃开发初期。
- 当前版本已整合WPS/Office/Zotero/Illustrator/Photoshop五大模块，CLI命令基本完备。
- 未来可能补充更多Adobe软件操控或跨平台能力（README未说明）。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：SVG-to-PPTX功能在README中未见具体实现方式或命令；项目根目录结构与各子模块的实际路径未完全展示，安装指引中的相对路径需用户自行匹配；未说明WPS/MS Office COM自动化在多线程或远程环境下的稳定性与限制；未提及是否支持Microsoft 365云版本或Office Online；Adobe软件操控仅支持Windows且需对应版本，未给出错误处理或降级方案