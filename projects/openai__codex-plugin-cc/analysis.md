## 它是什么
一个Claude Code插件，让开发者在使用Claude Code时可以直接调用OpenAI Codex的服务。它通过复用本地Codex CLI和认证，提供`/codex:review`、`/codex:adversarial-review`等只读审查命令，以及`/codex:rescue`、`/codex:transfer`等任务委派和会话移交命令，所有任务均可选择在后台运行并通过`/codex:status`和`/codex:result`管理。

## 为什么火
Star数高达22k+，因为解决了AI编程工具链中的一个真实痛点：在Claude Code中编码时，若想用Codex进行深度审查或长任务，无需切换工具或复制上下文。它让两个AI助手在同一代码仓上协同，并提供后台执行模式，使开发者不被长任务阻塞。加上OpenAI官方维护，信任度高。

## 技术栈
- 语言：JavaScript
- 运行时：Node.js 18.18+
- 核心依赖：本地Codex CLI及App Server（通过全局`codex`二进制）
- 配置：复用Codex的`config.toml`（用户级/项目级）
- 集成方式：Claude Code插件市场安装，通过斜杠命令和子代理（`codex:codex-rescue`）交互

## 核心能力
- **代码审查**：`/codex:review`（标准只读审查，支持`--base`分支对比）、`/codex:adversarial-review`（可定向挑战设计决策与风险区域，支持额外聚焦文本）
- **任务委派**：`/codex:rescue` 将调试、修复等任务交给Codex子代理，支持`--background`、`--resume`、`--fresh`和模型/努力级别选择
- **会话移交**：`/codex:transfer` 将当前Claude Code会话上下文转为Codex持久线程，生成`codex resume`命令
- **后台管理**：`/codex:status`、`/codex:result`、`/codex:cancel` 让用户异步跟踪和停止任务
- **审查门禁**：可选的`Stop`钩子，在Claude生成输出后自动运行Codex审查，若发现问题则阻止输出
- **配置透传**：直接使用Codex现有配置，支持项目级或用户级模型与推理努力设置

## 适用场景
1. **审查前发版**：用`/codex:review --base main`做快速分支审查
2. **对抗性压力测试**：对关键代码用`/codex:adversarial-review`挑战架构和边界情况
3. **持续调试**：Claude Code中遇到报错，用`/codex:rescue --background`让Codex并行调查
4. **跨工具协作**：在Claude Code开始调试，通过`/codex:transfer`移交到Codex TUI继续

## 同类对比
- **仅用Codex App/TUI**：需切出Claude Code，丧失上下文和流内体验；本插件保持在同一IDE/终端环境
- **其他AI助手插件**：如使用GitHub Copilot的代码审查，但本插件特性在于双向委托和会话移交，且完全使用Codex的强大审查能力
- **纯粹Claude Code内任务**：缺少专业审查视角和Codex的模型多样性，本插件补充了外部AI的第二意见

## 版本动态
v1.0.5新增`/codex:transfer`命令，实现Claude Code到Codex的会话移交，强化了双工具之间的工作流连续性。该版本也包含版本号更新和内部改进。项目维护活跃，由OpenAI团队迭代。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供审查质量或与Codex原生审查的对比数据；未说明后台任务最大并发数限制；未提及操作系统的明确支持列表（仅提到Node.js，隐含跨平台）；未描述错误恢复与重试策略；未给出`/codex:adversarial-review`的具体审查维度差异的量化说明