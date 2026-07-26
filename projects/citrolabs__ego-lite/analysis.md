## 它是什么
ego lite 是一款为 AI 代理和用户并行工作设计的桌面浏览器。它继承 Chrome 数据，提供隔离的“空间”让代理执行网页自动化任务，用户继续正常浏览不冲突。

## 为什么火
3k+ stars，2026年4月发布。解决了现有浏览器自动化框架需要额外驱动浏览器、登录状态无法共享、用户与代理争用标签页等痛点。通过直接在浏览器内提供 JavaScript 工具，代理能编写多步脚本，大幅减少 token 消耗和延迟。自称比同类快 2.5 倍。

## 技术栈
- 语言: JavaScript
- 跨平台: 当前仅 macOS，计划 Windows/Linux
- 关键组件: ego lite 应用，ego-browser 技能 (通过 npx skills add 安装)
- 核心技术: 基于内核级自定义的页面快照，Playwright 命名和单位的对齐 (内部可能采用 Playwright 或类似方案)

## 核心能力
- 多代理并行：每个代理一个空间，互不干扰
- 直接代码驱动：代理调用 JS 函数 (snapshot, fill, click 等) 而非 CLI 循环，减少 token 消耗
- 继承 Chrome 数据：登录、cookies、扩展、书签一键迁移
- 强页面快照：处理深层 iframe 等复杂情况
- 技能积累：即将推出，提取成功操作，加速后续类似任务

## 适用场景
- 使用 CLI 代理如 Claude Code、Codex 进行网页自动化
- 需要多个代理同时执行采集、填充、测试等任务
- 不想额外安装浏览器，希望复用已有登录状态的用户

## 同类对比
与 Browser-Use、agent-browser 等框架不同，ego lite 自带浏览器，无需额外驱动，登录继承。与 AI 浏览器 (ChatGPT Atlas, Perplexity Comet) 相比，它不内置代理，而是让外部代理控制，更加开放。

## 版本动态
当前 v1.2.5 (2026-07-17)。Release 修正了键盘/指针输入可靠性，增加了测试覆盖率，移除了 nightly 发布通道，改进了任务空间终止逻辑。项目活跃。
---

## ℹ️ 置信度与信息盲区

- 置信度：**medium**
- 信息盲区：未公开浏览器内核（是否基于 Chromium 等）；benchmark 具体数值缺失，仅图表；Windows/Linux 支持时间表不明确；技能积累功能尚未发布（README 称 coming soon）