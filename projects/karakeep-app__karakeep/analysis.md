## 它是什么
Karakeep（原Hoarder）是一个“万物书签”应用，可保存链接、笔记、图片和PDF，内置AI自动标签和全文搜索，专为数据囤积者打造。

## 为什么火
- 仅一年半获26k+ stars，填补了Pocket关闭后的市场缺口。
- 开源自托管，AI标签支持本地模型（ollama），保护隐私又智能。
- 拥有Chrome/Firefox/Safari扩展和iOS/Android应用，多端体验统一。
- 活跃的社区和商业化云服务，确保长期维护。

## 技术栈
- **前端**: Next.js (app router)、React Native（移动端）
- **后端**: tRPC + Next.js API
- **ORM**: Drizzle（推测底层为PostgreSQL）
- **搜索**: Meilisearch
- **爬虫**: Puppeteer + SingleFile
- **AI**: OpenAI 或通过 Ollama 运行本地模型
- **认证**: NextAuth（支持SSO）
- **其他**: REST API、RSS抓取、monolith/web存档

## 核心能力
- 自动抓取链接预览、标题和图片。
- AI自动标签和摘要，可结合规则引擎精细管理。
- 全文搜索与OCR图片文字提取。
- 协作列表，与他人共享书签。
- 导入支持Pocket、Linkwarden、Omnivore、Chrome书签等，可同步浏览器书签。
- 全页存档防链接失效，视频自动归档（yt-dlp）。
- AI Agent友好的CLI和官方技能，容易集成到自动化工作流。

## 适用场景
- 个人知识库：收藏文章、推文、工具链接并智能分类。
- 团队共享书签：协作列表搭配标签过滤快速检索。
- 自托管爱好者替代Pocket，追求数据主权。
- 与LLM工具链（如OpenClaw）结合，作为外部记忆或数据源。

## 同类对比
- **Pocket**：已死，Karakeep开源且功能持续迭代。
- **Linkwarden**：专注链接协作，Karakeep多格式支持和AI能力更强。
- **Wallabag**：PHP成熟项目，但Karakeep技术栈更现代，移动端体验更好。
- **memos**：轻量笔记，Karakeep是带预览和自动归类的完整书签系统。
- **mymind**：商业闭源，Karakeep提供完全开源替代。

## 版本动态
- v0.32.0（2026-05-08）核心更新：移动端大改版，Safari扩展正式上线，增强AI Agent集成（CLI、技能）、细粒度API密钥，SingleFile内建提升认证页面抓取，键盘快捷键等。
- 路线图包含离线阅读、语义搜索，社区贡献活跃。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：README 未明确指定数据库类型（推测为 PostgreSQL），也未提供 docker-compose 示例文件；缺少性能基准测试数据（如大规模书签下的搜索响应时间、资源占用）；移动端离线阅读等功能仍为计划中，未给出实现时间表；与 LLM Agent 集成的详细配置教程在 README 中缺失，需查阅文档