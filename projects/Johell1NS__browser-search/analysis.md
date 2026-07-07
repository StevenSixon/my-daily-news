## 它是什么
browser-search 是一份写给 AI 代理（OpenCode/Claude Code 等）的技能文件，指导代理通过三个开源工具完成网络搜索与浏览：SearXNG（元搜索）、Camofox（Firefox REST API 浏览器）、CloakBrowser（隐身 Playwright 浏览器）。代理能自动选择工具，遇到反爬站点自动升级到隐蔽浏览器，所有组件免费自托管，无 API 限流。

## 为什么火
1. **终结代理幻觉**：强制“先搜再答”工作流，每个事实需多角度交叉验证，绝不编造。
2. **零成本反封锁**：Cloudflare、Akamai 等反爬不再是障碍，CloakBrowser 58 条 C++ 底层补丁 + 类人指纹通过几乎所有测试，彻底告别付费反反爬服务。
3. **极简集成**：一行 `npx skills add` 后 AI 代理自动读取文档并适配环境，无需手写胶水代码。
4. **全本地无限量**：完全在本地运行，无 API 密钥、无订阅、无速率限制，树莓派都跑得动。

## 技术栈
- **语言/运行时**：Node.js (ESM 模块)
- **搜索层**：SearXNG (Docker) → 多引擎聚合，返回 JSON
- **常规浏览**：Camofox (Docker) → Firefox 内核 + REST API，内置 Readability.js 清洗正文
- **隐身浏览**：CloakBrowser (npm) → Playwright + Chromium，自动检测并绕过反爬挑战
- **技能定义**：SKILL.md (纯文本)，跨代理通用

## 核心能力
- **智能编排**：代理自主决策使用 SearXNG 搜索、Camofox 浏览、CloakBrowser 突破封锁
- **自动逃生**：Camofox 被 Cloudflare 阻断时自动升级到 CloakBrowser，覆盖 ~90% 普通站点 + ~10% 防护站点
- **反幻觉模式**：深度研究工作流强制事实核查，对抗大模型幻觉
- **隐身引擎**：CloakBrowser 实现 0.9 reCAPTCHA v3 人类级评分，通过 Cloudflare Turnstile
- **轻量持久**：Camofox 常驻热容器，首次冷启动后所有请求近乎实时；CloakBrowser 按需启动

## 适用场景
- AI 编码助手需要查阅最新文档或社区讨论
- 自主代理执行深度研究（如市场分析、竞品情报）
- 低资源设备（树莓派）上搭建个人 RSS/爬虫代理
- 绕过严格反爬的网站抓取原型验证

## 同类对比
- **vs. 付费搜索 API（Tavily/SerpAPI）**：完全本地、零成本、无限量，但需自己维护基础设施。
- **vs. 单独使用 Playwright Stealth**：本技能提供快速浏览（Camofox）与高隐身（CloakBrowser）的自动切换，避免所有请求都用重量级隐身代理造成的延迟。
- **vs. Perplexity 等闭源产品**：开源、可审计、可自定义规则，敏感数据不离开自己机器。

## 版本动态
v1.2.0 (2026-07-07) 主要优化健康检查、修正默认输出格式、更新 Camofox 官方镜像引用、依赖升级 cloakbrowser 0.4.8，并重写中英文等多语言文档与安全说明。项目处于活跃迭代期。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供 Docker Compose 或一键部署脚本，需用户自行配置 SearXNG 和 Camofox 容器；CloakBrowser 的实际反爬成功率缺乏独立第三方验证；未展示与其他 AI 搜索工具（如 Tavily、Exa）的直接性能/成本对比；FAQ 文档仅修复链接但未展示全文，其问题解答细节不明；缺少针对不同操作系统（Windows/macOS）的具体部署注意事项