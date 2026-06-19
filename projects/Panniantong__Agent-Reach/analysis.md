## 它是什么
Agent Reach 是一个面向 AI Agent（Claude Code、Cursor、OpenClaw 等）的「能力层」——不是另一个工具，而是一键安装+路由层。它自动选型、装好并体检 Twitter/Reddit/YouTube/B站/小红书/LinkedIn/GitHub 等多个平台的最佳免费接入方式。一句指令就能让 Agent 拥有搜索与阅读全互联网的能力，无需开发者逐一折腾 API Key、反爬策略与登录态。

## 为什么火
项目Star超三万，核心卖点是“零API费+持续抗封”。传统开发者让Agent上网，要对接Twitter付费API、绕过Reddit匿名封锁、适配B站风控，时间成本极高。Agent Reach用实测多后端路由（首选+备选）思路化解平台换代风险，2026-06已两次应对大厂封锁（yt-dlp被B站封、Reddit匿名接口关闭），用户无感知。安全透明（本地存Cookie+开源+MCP免费搜索）也打消了隐私顾虑。

## 技术栈
- 语言：Python 3.10+，CLI 框架；agent-reach 本体通过 pip 分发
- 上游工具（多后端路由）：twitter-cli/OpenCLI、rdt-cli、bili-cli、yt-dlp、feedparser、Exa（mcporter MCP）、gh CLI、xiaohongshu-mcp 等
- 安装基建自动检测 Node.js、npm、mcporter；可安全模式/Dry Run
- 桌面端引入 OpenCLI（Chrome 扩展）复用浏览器登录态
- 测试：107→162 项契约/端到端测试，13 渠道 32 项实测

## 核心能力
1. **全平台读取**：YouTube 字幕/搜索、B站/video详情（无登录）、Twitter 推文/搜索、Reddit 帖子/评论、小红书笔记/搜索、GitHub 仓库/Issue、LinkedIn、V2EX、雪球、RSS 等
2. **智能路由与体检**：每个平台多条后端正序检测，自动切换到当前可用后端；`agent-reach doctor --json` 输出当前活跃后端并给出修复处方
3. **全网语义搜索**：通过 Exa MCP 免费接入，无需 Key
4. **安全与隐私**：本地 Cookie 不通天、600 权限、可安全模式预览、可卸载清凭据
5. **Agent 自动技能注入**：安装时注册 SKILL.md，Agent 遇“全网调研”等自然语言自动调用正确上游命令

## 适用场景
- 让任何可执行 shell 的 AI Agent（Claude Code、Cursor、OpenClaw、Windsurf）直接拥有互联网阅读能力
- 产品调研：快速抓取推特评价、Reddit 讨论、小红书口碑、YouTube 教程总结
- 开发辅助：B站技术视频总结、GitHub Issue 分析、RSS 监控更新
- 信息聚合：全网语义搜索+多源交叉验证，无需付费 API
- 个人或小团队零成本搭建 Agent 信息基础设施

## 同类对比
- 相比 LangChain/Tools 生态中的独立加载器（如 Tweepy、praw）需要逐个申请 API Key、处理额度与封号，Agent Reach 主打“零配置+免费+自动换路”。
- 相比 Browserless/Playwright 方案，Agent Reach 更轻量、不依赖无头浏览器（除小红书服务器备选），优先使用 CLI 工具，延迟低。
- 相比官方 API（Twitter $100/月、Reddit 审批制）几乎免费，利用登录态和开源工具和平访问。
- 独特优势：路由层抽象，平台封杀后用户零操作，适合非技术人员通过 Agent 间接使用。

## 版本动态
- v1.5.0（2026-06-11）重大升级：引入 OpenCLI 桌面后端，实现小红书/Reddit 零配置（浏览器登录态复用）；B站 yt-dlp 退役，切换至 bili-cli；doctor 升级为真探测修复建议，输出当前活跃后端；新增 install/update 一句话拉起；测试项 107→162，三轮对抗性 review 修复 12 项关键问题。
- 项目始于 2026-02，MIT 许可，社区动态显活跃（Issue/PR 接受新渠道请求）。