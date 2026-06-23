## 它是什么
HyperFrames 是一个开源视频渲染框架，核心思路是把 HTML/CSS/动画“剧本”直接转成确定性 MP4 视频。它提供 CLI、预览和渲染流水线，并专门为 AI 编程代理设计了技能（Skills），让代理也能像写网页一样制作视频。

## 为什么火
30k+ Star 的背后是“一切皆可视频”的工程化需求。开发者厌倦了 React 驱动的视频引擎，而 HyperFrames 的 **纯 HTML + 数据属性** 模式大幅降低了门槛——对人或对代理都友好，且**渲染结果完全可重现**，适合 CI 流水线、自动化内容生产。

## 技术栈
- **语言/运行时**：TypeScript，Node.js ≥ 22
- **渲染核心**：Puppeteer（headless Chrome）+ FFmpeg 编码
- **动画支持**：GSAP、CSS/WAAPI、Lottie、Three.js 等，通过全局时间线注册
- **构建与分发**：npm 包，支持本地 CLI、Docker、云函数（AWS Lambda/GCP/K8s）

## 核心能力
- **HTML 即 composition**：用 `index.html` 定义片段时间、轨道、媒体，零构建步骤
- **确定帧渲染**：同一输入、同一输出，保障回归测试和自动化 pipeline
- **代理技能**：针对 Claude Code/Cursor 等编码代理的专用技能，教代理理解视频制作循环
- **Catalog 组件库**：即装即用的转场、字幕、图表等模块（`npx hyperframes add ...`）
- **frame.md 设计系统**：将品牌设计 token 转化为视频可用的规范，方便代理或设计师复用

## 适用场景
- 产品发布视频、PR 动画说明（代码 diff、旁白、字幕）
- 数据可视化视频（动态图表、地图动画）
- 社交媒体短视频生成（大字标题、音效、音乐）
- Agent 驱动的文档/PDF/网站转视频，自动内容管道

## 同类对比
与 Remotion 相比，最大的差异在作者模型：Remotion 用 React，HyperFrames 用**纯 HTML**。后者对非前端开发者及 AI 代理更友好，且无需 React 环境，降低集成成本。但仍依赖 headless Chrome 和 FFmpeg，渲染原理相似。

## 版本动态
最新 v0.7.2（2026-06-22）修复了 shader 转场抓取、音频时长保持、CSS 变量字体解析等生产环境边缘问题，并增强了回归测试覆盖。项目活跃，正逐步完善云端渲染部署示例（AWS Lambda、GCP Cloud Run、K8s Jobs）。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供渲染性能基准和并发上限数据；未说明 headless Chrome/FFmpeg 具体版本兼容性；缺乏大规模分布式渲染的最佳实践文档；未展示极端动画场景下的确定性验证结果