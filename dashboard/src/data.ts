// Real data sourced from the my-daily-news pipeline output
// daily/2026-06-19.json + projects/<name>/metadata.json + analysis.md

export interface AnalysisSection {
  heading: string;
  body?: string;
  bullets?: string[];
}

export interface Project {
  id: string;
  fullName: string;
  owner: string;
  name: string;
  url: string;
  oneLiner: string;
  description: string;
  language: string;
  category: string;
  license: string;
  starsTotal: number;
  starsGained: number;
  streakDays: number;
  isNew: boolean;
  createdAt: string;
  pushedAt: string;
  latestRelease: string;
  firstSeen: string;
  topics: string[];
  analysis: AnalysisSection[];
}

export interface Daily {
  date: string;
  count: number;
  projects: Project[];
}

export const daily: Daily = {
  date: "2026-06-19",
  count: 2,
  projects: [
    {
      id: "agent-skills",
      fullName: "addyosmani/agent-skills",
      owner: "addyosmani",
      name: "agent-skills",
      url: "https://github.com/addyosmani/agent-skills",
      oneLiner:
        "为 AI 编码代理提供覆盖全生命周期的 24 个生产级工程技能，让代理遵循资深工程师的规范与质量实践。",
      description: "Production-grade engineering skills for AI coding agents.",
      language: "Shell",
      category: "AI 应用",
      license: "MIT",
      starsTotal: 63206,
      starsGained: 9285,
      streakDays: 1,
      isNew: true,
      createdAt: "2026-02-15",
      pushedAt: "2026-06-19",
      latestRelease: "0.6.2",
      firstSeen: "2026-06-19",
      topics: ["agent-skills", "antigravity", "antigravity-ide", "claude-code", "cursor", "skills"],
      analysis: [
        {
          heading: "它是什么",
          body: "Agent Skills 是一套面向 AI 编码代理的生产级工程技能包，由 Google Chrome 开发者关系负责人 Addy Osmani 维护。它把资深工程师在软件开发全生命周期中使用的工作流、质量关卡和最佳实践打包成 24 个结构化技能，通过 7 个斜杠命令（/spec、/plan、/build、/test、/review、/code-simplify、/ship）自动激活，覆盖从想法精炼到生产交付的每个环节。技能以 Markdown 编写，与任何能读取系统提示或指令文件的 AI 代理兼容，内置反模式表、验证步骤和安全边界。",
        },
        {
          heading: "为什么火",
          body: "项目在短时间内获得 63k+ Star，成为 AI 辅助开发领域的热点。核心原因：1）填补了 AI 代理“会写代码但不懂工程纪律”的空白——代理往往能生成正确代码，却忽略测试策略、安全审查、性能约束等工程上下文；2）标准化程度高，一套技能可跨 Claude Code、Cursor、Copilot、Gemini CLI、Antigravity 等工具复用；3）由 Addy Osmani 和众多贡献者持续打磨，引入威胁建模、可观测性、浏览器性能审计等现代工程主题；4）社区驱动，PR 活跃，快速适配新 IDE 和 CLI，且许可证宽松（MIT）。",
        },
        {
          heading: "技术栈",
          bullets: [
            "技能格式：Markdown + 结构化工作流指令，利用原生 AI 系统的 prompt/rule 机制。",
            "支持平台：Claude Code（官方插件市场）、Antigravity CLI（原生插件）、Cursor（.cursor/rules/）、GitHub Copilot（agents/ 代理定义）、Gemini CLI、Windsurf、OpenCode、Kiro 以及任意可注入指令的工具。",
            "关键依赖：自身不依赖特定运行时，仅用 Markdown。在浏览器测试技能中使用 Chrome DevTools MCP 协议进行运行时交互；可观测性技能引入 OpenTelemetry 等最佳实践。",
            "自动化：通过 /build auto 一键生成计划并全自动实施，保留按任务独立提交和测试验证。",
          ],
        },
        {
          heading: "核心能力",
          bullets: [
            "全生命周期命令：/spec（定义需求）→ /plan（拆解任务）→ /build（增量实现）→ /test（验证）→ /review（质量审查）→ /code-simplify（简化代码）→ /ship（交付上线）。",
            "24 项技能：涵盖元技能、用户访谈、想法精炼、规范驱动开发、任务拆解、增量实现、TDD、上下文工程、源码驱动开发、怀疑驱动开发、前端工程、API 设计、浏览器 DevTools 测试、调试纠错、代码审查、代码简化、安全加固、性能优化、Git 工作流、CI/CD、弃用迁移、文档与 ADR、可观测性、发布上线。",
            "代理角色：预配置的代码审查员、测试工程师、安全审计员、性能审计员等 specialist 角色，直接调用。",
            "安全增强：最新版加入威胁建模、SSRF 防护、供应链及 AI/LLM 专项安全技能。",
            "可观测性：RED 指标、结构化日志、分布式追踪、基于症状的告警模式。",
          ],
        },
        {
          heading: "适用场景",
          bullets: [
            "使用 AI 编码工具的个人开发者或团队，希望强制代理遵守 TDD、代码审查、安全扫描等工程纪律。",
            "从零到一的绿场项目，用 /spec → /build auto 快速产出一致、可验的代码基。",
            "棕场遗留系统改造：通过安全加固、性能优化、代码简化等技能进行系统化治理。",
            "跨工具协同：同一套技能在 Claude Code 和 Cursor 等不同 IDE 间保持一致，降低团队认知成本。",
            "教育与 onboarding：新成员通过技能指令学习资深工程师的决策习惯和质量标准。",
          ],
        },
        {
          heading: "同类对比",
          bullets: [
            "与 cursor-rules、copilot-instructions 等相比：多数项目仅提供散装 best-practice 提示词或特定语言模板，Agent Skills 是一套正交于语言/框架的工程方法论，有清晰的生命周期映射和反模式防御。",
            "与 DevQualityGPT 等质量工具相比：更偏重于代理执行过程中的即时约束，而非事后检查。",
            "与 OpenHands、Aider 等编码代理自带指令相比：Agent Skills 强调可移植，不绑定单一平台，且覆盖从需求到部署的全过程，更为系统化。",
            "独特点：引入“怀疑驱动开发”、源码驱动开发、上下文工程等元技能，将软件设计层面的思维模式代码化。",
          ],
        },
        {
          heading: "版本动态",
          bullets: [
            "当前版本 0.6.2（2026-06-11），上一版本 0.6.1。",
            "本次更新：修复市场安装中 SSH/HTTPS 问题；将安全技能扩展为包含威胁建模、SSRF、供应链及 AI/LLM 攻击面的深度技能。",
            "新增 web-performance-auditor 代理和 /webperf 命令；新增 observability-and-instrumentation 技能；新增 Antigravity CLI 原生支持（agy plugin install）。",
            "社区贡献者活跃，发布节奏稳定，项目仍处于快速发展期。",
          ],
        },
      ],
    },
    {
      id: "headroom",
      fullName: "chopratejas/headroom",
      owner: "chopratejas",
      name: "headroom",
      url: "https://github.com/chopratejas/headroom",
      oneLiner: "压缩 AI 代理上下文，节省 60-95% token 且答案不变。",
      description:
        "Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers. Library, proxy, MCP server.",
      language: "Python",
      category: "AI 应用",
      license: "Apache-2.0",
      starsTotal: 36949,
      starsGained: 10159,
      streakDays: 1,
      isNew: true,
      createdAt: "2026-01-07",
      pushedAt: "2026-06-19",
      latestRelease: "v0.26.0",
      firstSeen: "2026-06-19",
      topics: [
        "agent", "ai", "anthropic", "claude-code", "compression", "context-engineering",
        "context-window", "cursor", "fastapi", "langchain", "llm", "mcp", "openai",
        "prompt-engineering", "proxy", "python", "rag", "token-optimization", "tokens", "typescript",
      ],
      analysis: [
        {
          heading: "它是什么",
          body: "Headroom 是一个上下文压缩层，在代理向 LLM 发送数据前压缩工具输出、日志、文件、RAG 块和对话历史，减少 60-95% token 使用，同时保持相同答案。它提供库、代理服务器、MCP 服务器和代理包装器，支持 Claude Code、Cursor、Codex 等主流编程代理。",
        },
        {
          heading: "为什么火",
          bullets: [
            "真实代理负载节省显著：代码搜索压缩 92%，SRE 调试压缩 92%。",
            "基准测试准确性无损失：GSM8K、TruthfulQA 等性能不变，TruthfulQA 甚至提升 0.03。",
            "零代码改动集成：代理包装器、MCP 工具、drop-in 代理服务器。",
            "可逆压缩（CCR）：本地缓存原始内容，LLM 可按需检索。",
            "智能学习：headroom learn 挖掘失败会话，写入建议至 CLAUDE.md。",
            "输出 token 缩减：修剪模型冗长输出，进一步降低成本。",
          ],
        },
        {
          heading: "技术栈",
          bullets: [
            "语言：Python（主）、TypeScript。",
            "压缩算法：SmartCrusher（JSON）、CodeCompressor（AST）、Kompress-base（Hugging Face 模型 Kompress-v2-base）。",
            "架构：CacheAligner（KV 缓存命中优化）、ContentRouter（内容类型路由）、CCR（可逆存储）。",
            "集成：FastAPI 代理，支持 LangChain、Vercel AI SDK、MCP。",
            "平台：Anthropic、OpenAI、AWS Bedrock 等。",
          ],
        },
        {
          heading: "核心能力",
          bullets: [
            "库调用：compress(messages) 一行压缩。",
            "代理服务器：headroom proxy --port 8787，任何语言可用。",
            "代理包装：headroom wrap claude/codex/cursor/aider/copilot。",
            "MCP 服务器：提供 headroom_compress、headroom_retrieve、headroom_stats 工具。",
            "跨代理内存共享与自动去重。",
            "输出 token 缩减：冗长度引导与努力路由减少模型输出浪费。",
            "学习模块：根据历史会话学习最优压缩和冗长度。",
            "可逆压缩：CCR 存储原始数据，动态检索。",
          ],
        },
        {
          heading: "适用场景",
          bullets: [
            "编码代理（Claude Code、Cursor 等）降低 token 成本。",
            "大规模 RAG 压缩检索块。",
            "SRE/运维调试压缩大量日志。",
            "多代理协作共享压缩内存。",
            "任何需要优化 LLM 上下文窗口的应用。",
          ],
        },
        {
          heading: "同类对比",
          body: "与其他 prompt 压缩库相比，Headroom 提供多算法路由、可逆压缩和跨代理内存，并优化输出；与简单 prompt 缓存相比，CacheAligner 主动调整前缀以提高 KV 缓存命中率，结合压缩效果更佳，且具备学习功能和仪表板监控。",
        },
        {
          heading: "版本动态",
          body: "v0.26.0（2026-06-16）新增：Copilot BYOK 包装器、仪表板代理统计、Mistral Vibe CLI 支持、重读浪费归因、Bedrock 跨区域压缩、前缀缓存面板净影响展示、对抗性输入鲁棒性评估网格、同工具重发检测、批量深度编辑优化等。社区活跃，持续迭代。",
        },
      ],
    },
  ],
};
