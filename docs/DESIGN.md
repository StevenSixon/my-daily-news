# AI 项目日报助理 — 技术设计文档

> 版本：v1.0　|　日期：2026-06-19　|　状态：待评审
> 一句话目标：每天自动发现 GitHub 上爆火的 **AI 应用类**项目，深度学习并归档到本地，每天早上 8:00 通过飞书机器人推送简短汇报。

---

## 1. 目标与范围

### 1.1 要解决的问题
作为技术极客，想及时跟进 GitHub 近期爆火的 AI 项目，但没时间逐个看。需要一个助理：自动发现 → 自动学习 → 本地归档 → 每天早上推送简短汇报。

### 1.2 本期范围（v1）
- ✅ 定时采集近期爆火的 **AI 应用相关**项目（双数据源：GitHub Trending + Search API）
- ✅ 对每个新项目做**中档深度**学习（README + 关键文档 + release），产出结构化报告
- ✅ 每个项目在本地有独立目录，文档有序，便于按需深入
- ✅ 每天 08:00 通过飞书自定义机器人推送简短汇报（带本地报告指引）
- ✅ 去重：同一项目不重复学习；持续上榜做"连续 N 天"标注
- ✅ **Web 看板（v1.x 已补充，超出最初 v1 范围）**：React 单文件 artifact，由流水线产物经 `dashboard/scripts/gen-data.mjs` 生成，`refresh.sh` 自动"刷新→提交→推送"，GitHub Pages 自动部署。含多日切换、累计排行榜、分类/语言筛选、上榜走势图、移动端响应式。详见 `dashboard/README.md`

### 1.3 暂不做（留待后续）
- ❌ 深度拆解源码级架构分析（成本高）。建议做成**按需触发**的单仓库命令（如 `python -m src.deepdive <owner/repo>` → 写入 `projects/<name>/deepdive.md`，看板详情页加「深度专题」分区展示），并设门槛：只对**连榜多日 / 累计涨幅 top** 的项目才深挖，避免逐个跑。
- ❌ 非 AI 应用类目（架构上预留扩展位，靠 config 切换）。建议未来作为**独立频道**扩展（独立 config + 独立飞书接收 + 看板频道切换），而非混进同一份 AI 榜单——以免稀释定位、抬高候选量与 LLM 成本。
- ~~Web UI / 移动端~~ → 已于 v1.x 交付（见 1.2）。

### 1.4 设计原则
> **采集、推送 = 确定性脚本（可靠、便宜）；只有"学习"这一步调用大模型。**
> 不让 LLM 去做抓取、发消息这类脏活——既贵又不稳。

---

## 2. 总体架构

运行环境：**本地 Mac，launchd 定时调度**。整条流水线为普通 Python 脚本，仅 `analyze` 阶段调用 Claude API。

```
┌──────────────────────────────────────────────────────────────────┐
│  launchd 触发（错峰）                                               │
│                                                                    │
│  06:30  ① collect.py  采集 + 过滤 + 去重                            │
│         ├─ GitHub Trending 抓取（daily/weekly）                     │
│         ├─ GitHub Search API（topic:ai/llm/agent + 时间窗 + star）  │
│         ├─ 合并去重 → LLM 轻量分类，只留"AI 应用"                    │
│         └─ 与 data/seen-repos.json 比对 → 输出当天"新项目清单"        │
│                         ↓                                          │
│  06:35  ② analyze.py  深度学习（逐项目，中档）                       │
│         ├─ 拉取 README / docs / 最新 release / metadata             │
│         ├─ Claude API 生成 analysis.md / quickstart.md / 一句话摘要 │
│         └─ 写入【项目库】projects/<owner__repo>/（原地迭代）          │
│            · 新项目→新建目录；已存在→更新报告 + 追加 history 一条     │
│                         ↓                                          │
│  06:50  ③ build_summary.py  汇总当天日报                            │
│         └─ 生成【日报】daily/<日期>.md（轻量，引用项目库）            │
│                         ↓                                          │
│  08:00  ④ push.py  飞书推送                                         │
│         └─ 读取 daily-summary → 飞书 webhook 发交互卡片             │
└──────────────────────────────────────────────────────────────────┘
```

**为什么 06:30 采集、08:00 推送错峰？**
学习耗时不可控（项目多/网络慢/模型排队），提前在凌晨跑完，08:00 只做"读取已生成的总览并发送"，保证准时、可靠。即使学习阶段部分失败，08:00 仍能推送已完成的部分。

---

## 3. 模块详细设计

### 3.1 ① collect.py — 采集

**数据源 A：GitHub Trending**
- 目标：`https://github.com/trending?since=daily`（及 `weekly`）
- GitHub 无官方 Trending API → HTML 抓取（requests + selectolax/bs4）
- 解析字段：repo 全名、描述、语言、总 star、**当期新增 star**（Trending 页面直接给出"X stars today/this week"，省去自己算周增长）
- 价值：最贴近"爆火"直觉

**数据源 B：GitHub Search API**（官方、稳定、可精确过滤 AI）
- 端点：`GET /search/repositories`
- 查询示例：
  ```
  q = "topic:ai OR topic:llm OR topic:agent OR topic:rag OR topic:llm-agent
        created:>=<近30天> stars:>200"
  sort = stars, order = desc
  ```
- 配合 `pushed:>=<近7天>` 过滤近期活跃项目
- 价值：可按主题精确锁定 AI；补 Trending 漏掉的细分项目
- 注意：未认证 60 次/h，带 token 5000 次/h → **必须配置 GitHub PAT**

**合并与过滤流程**
1. 两源结果按 `full_name` 合并去重
2. **LLM 轻量分类**（一次性批量调用）：把候选列表的 `名称+描述+topics` 喂给 Claude，判定每个是否属于"AI 应用"（区别于纯 ML 框架/数据集/论文复现），输出 `keep: true/false + 理由 + 标签`
3. 与 `data/seen-repos.json` 比对，过滤已学过的
4. 按"当期新增 star"排序，取 Top N（config 配置，默认 5）

**输出**：`当天新项目清单`（内存对象，传给 analyze）+ 持续上榜项目的"连续天数 +1"

---

### 3.2 ② analyze.py — 深度学习（中档）

对每个新项目：

**输入上下文（喂给 Claude）**
| 内容 | 来源 |
|---|---|
| README（截断到合理长度） | `GET /repos/{o}/{r}/readme` |
| 仓库元数据 | `GET /repos/{o}/{r}`（star、language、topics、license、created/pushed） |
| 最新 release / CHANGELOG | `GET /repos/{o}/{r}/releases/latest` |
| 关键文档（docs/、examples/ 的索引） | `GET /repos/{o}/{r}/contents/docs` 等，仅取目录与首篇 |

**输出位置：项目库 `projects/<owner__repo>/`（与日期无关，持续迭代）**
| 文件 | 内容 | 迭代策略 |
|---|---|---|
| `metadata.json` | 结构化元数据 + 上榜/star 历史（见 §4.2） | 每次复访**原地更新**，历史追加进数组 |
| `analysis.md` | 深度学习报告：①它是什么 ②为什么火 ③技术栈 ④核心能力 ⑤适用场景 ⑥同类对比 ⑦版本动态 | 有重要更新（新 release / 大幅涨 star）时**重生成覆盖** |
| `quickstart.md` | 如何 5 分钟跑起来：安装、最小示例、依赖前提 | 同上 |
| `history.md` | 迭代日志：每次被收录/再学习追加一行（日期 / 触发原因 / 当时 star / 变更摘要） | **只追加，不删** |
| `README.snapshot.md` | 最新 README 快照，便于离线回看 | 覆盖为最新；如需留版本可加 `README.snapshot.<日期>.md` |
| （一句话亮点） | 写回 metadata，供日报与飞书卡片用 | 更新 |

> **复访判定**：项目已在库中时，仅当检测到「最新 release 变更 / star 显著增长 / pushed_at 更新」才重新调用 LLM 重生成报告；否则只更新 metadata 的 star 与 streak，并在 history 追加一行轻量记录，**节省 API 成本**。

**Prompt 设计要点**
- 系统提示：扮演"资深技术分析师"，面向"想快速判断是否值得深入的极客"，**简洁、去营销话术、说人话**
- 强制结构化输出（固定小标题），便于跨项目对比
- 要求标注"信息来源/置信度"，README 里没写清的不要编

**成本控制**
- 每项目 1~2 次调用；Top N=5 → 每天约 5~10 次调用
- README 超长时先截断 + 摘要，避免无谓 token

**模型可插拔（重要）**
- analyze 不直接绑定 Claude，而是调用统一的 `llm_client.chat(messages)`（见 §3.6）。
- 用哪个模型完全由 `config.yaml` 的 `llm:` 段决定，换模型不改业务代码。

---

### 3.3 ③ build_summary.py — 当天日报

聚合当天命中的项目，生成**轻量**的 `daily/<日期>.md`（日报只做索引/快照，不重复正文）：
- 顶部：日期、当天新增/复访项目数、数据源
- 列表：每项目 = 名称 / 一句话亮点 / 当期新增 star / 语言 / GitHub 链接 / **指向项目库的相对路径** `../projects/<owner__repo>/analysis.md`
- 标注"🆕新发现" / "🔥连续上榜 N 天"

这份 md 同时是**人读的当天总览**和**飞书推送的数据源**。日报与项目库解耦：日报是「时间线」，项目库是「知识库」。

---

### 3.4 ④ push.py — 飞书推送（自建应用 / custom app）

> 注：本项目用的是**飞书自建应用**（App ID `cli_...` + App Secret），不是自定义机器人 webhook。

- 鉴权：`app_id + app_secret` → 调 `auth/v3/tenant_access_token/internal` 换 `tenant_access_token`（~2h 有效，**本地缓存复用**，过期前刷新）
- 发送：调 `im/v1/messages?receive_id_type=<open_id|email|mobile>`，`msg_type=interactive`（卡片）
- 接收者：**直接私聊推给你本人（P2P）**，不用群 `chat_id`。用你的 `open_id`（`ou_…`，最稳）或飞书注册邮箱/手机定位，配于 `.env` 的 `FEISHU_RECEIVE_ID` + `FEISHU_RECEIVE_ID_TYPE`
- 所需权限（飞书开放平台后台开启并发布应用）：`im:message`、`im:message:send_as_bot`
- 拿 `open_id` 的简单方式：① 飞书开放平台「API 调试台」用你的账号调一次拿到；② 你给我注册邮箱/手机，我用通讯录接口换（需 `contact:user.base:readonly` 权限）；③ 你先私聊机器人一句，应用收到消息事件里就带你的 `open_id`
- 卡片内容（简短优先）：
  - 标题：`🤖 AI 项目日报 · 2026-06-19`
  - 正文：当天 Top 3~5，每条 = `名称 + 一句话亮点 + ⭐当期新增 star + GitHub 链接`
  - 脚注：`📂 详细报告见本地项目库 projects/ （当天 N 个）`
- 失败重试：发送失败重试 2 次（注意 token 过期需重取），仍失败写 `logs/` 并可选降级为 macOS 系统通知

---

### 3.5 调度 — launchd

两个 launchd plist（或一个脚本内部串行 + 一个推送任务）：
- `com.daily-news.pipeline.plist`：06:30 跑 collect → analyze → build_summary
- `com.daily-news.push.plist`：08:00 跑 push

注意：
- Mac 睡眠会延迟触发 → 文档提示"保持唤醒或插电"，或用 `pmset` 唤醒；后续若迁服务器则用 cron
- 日志重定向到 `logs/`，便于排查

---

### 3.6 llm_client.py — 多模型抽象层（可插拔）

业务代码只依赖一个统一接口，**换模型只改配置、不改代码**。

**统一接口**
```python
# 所有上层（analyze 的轻量分类、深度报告）只调这一个函数
llm_client.chat(messages, *, system=None, max_tokens=None, json=False) -> str
```

**支持的 provider（config 选其一为主，可配降级链）**
| provider | 接入方式 | 典型模型 |
|---|---|---|
| `anthropic` | Anthropic SDK | claude-opus-4-8 / claude-sonnet-4-6 |
| `openai` | OpenAI SDK | gpt-4o / o-series |
| `gemini` | Google SDK | gemini-2.x |
| `deepseek` | OpenAI 兼容 | deepseek-chat / reasoner |
| `openai_compatible` | OpenAI SDK + 自定义 `base_url` | Moonshot / 本地 vLLM / 任意兼容端点 |
| `ollama` | 本地 `base_url`，无需 key | 任意本地模型 |

**实现策略**
- 首选用 **LiteLLM** 作为统一适配层（一个库覆盖上述绝大多数 provider，统一 `messages` 格式与返回）；它本身就是为"一套代码多模型"设计的。
- 如不引第三方，则用**适配器模式**：`BaseProvider` 抽象 + 各 provider 子类，`llm_client` 按 config 实例化对应子类。
- **降级链**：主模型调用失败（超时/限流/报错）→ 自动尝试 `fallback` 列表里的下一个，全失败才报错。
- **密钥与 base_url 全部从 `.env` 读**，provider 切换时只改 `config.yaml` 的 `llm.provider/model`。

> 收益：今天用 Claude，明天想用 DeepSeek 降本、或用本地 Ollama 离线跑，只改两行配置即可。

---

## 4. 数据模型与目录结构

### 4.1 目录结构

核心：**项目库（知识库，按项目，与日期无关）** 与 **日报（时间线，按天）** 分离。

```
my-daily-news/
├── docs/
│   └── DESIGN.md                     # 本文档
├── src/
│   ├── collect.py
│   ├── analyze.py
│   ├── build_summary.py
│   ├── push.py
│   ├── github_client.py              # GitHub API/Trending 封装
│   ├── llm_client.py                 # Claude API 封装
│   └── feishu_client.py              # 飞书自建应用 鉴权 + 卡片封装
├── config/
│   └── config.yaml
│
├── projects/                         # 【项目库】以项目为单位，持续迭代，与日期无关
│   └── owner__repo/                  # 每个项目一个固定目录（再上榜时原地更新）
│       ├── metadata.json             # 元数据 + 上榜/star 历史（持续更新）
│       ├── analysis.md               # 深度报告（有重要更新时重生成覆盖）
│       ├── quickstart.md             # 上手指南
│       ├── history.md                # 迭代日志（只追加：每次收录/再学习一行）
│       └── README.snapshot.md        # 最新 README 快照
│
├── daily/                            # 【日报】按天，轻量，引用项目库
│   └── 2026-06-19.md                 # 当天总览 = 飞书推送数据源
│
├── data/
│   └── index.json                    # 全局索引：项目→目录、去重、streak（见 §4.3）
├── logs/
│   └── 2026-06-19.log
├── .env                              # 密钥（不入库）
├── requirements.txt
└── README.md
```

**两者关系**：`daily/2026-06-19.md` 里每个条目用相对链接指向 `../projects/owner__repo/analysis.md`。删某天日报不影响项目库；项目库是长期沉淀的知识资产。

### 4.2 `projects/<owner__repo>/metadata.json`（单项目，持续迭代）
```json
{
  "full_name": "owner/repo",
  "url": "https://github.com/owner/repo",
  "description": "原始描述",
  "language": "Python",
  "topics": ["llm", "agent"],
  "license": "MIT",
  "category": "AI 应用",
  "one_liner": "一句话亮点（LLM 生成，最新）",

  "stars_total": 12450,
  "created_at": "2026-05-01",
  "pushed_at": "2026-06-18",
  "latest_release": "v0.4.2",

  "first_seen": "2026-06-15",
  "last_seen": "2026-06-19",
  "streak_days": 5,
  "analysis_updated_at": "2026-06-19T06:42:00+08:00",

  "appearances": [
    {"date": "2026-06-15", "reason": "new", "stars_total": 9800, "stars_gained": 1200, "release": "v0.4.0"},
    {"date": "2026-06-19", "reason": "release_update", "stars_total": 12450, "stars_gained": 820, "release": "v0.4.2"}
  ]
}
```
> 与日期无关的"项目档案"。`appearances[]` 记录每次上榜的快照，构成 star/版本的时间序列，便于后续趋势分析。

### 4.3 `data/index.json`（全局索引 + 去重 + 复访判定）
```json
{
  "owner/repo": {
    "dir": "projects/owner__repo",
    "first_seen": "2026-06-15",
    "last_seen": "2026-06-19",
    "streak_days": 5,
    "last_release_seen": "v0.4.2",
    "last_stars_total": 12450
  }
}
```
> **去重 + 复访策略**：
> - 不在索引 → 新项目，建目录、全量学习、`reason=new`。
> - 已在索引但 `latest_release` 变了 / star 显著增长 → **复访重学**，覆盖 analysis、`reason=release_update`。
> - 已在索引且无实质变化 → 不调 LLM，仅更新 `streak_days`/`last_seen` 并向 `history.md` 追加一行，日报标注"🔥连续 N 天"。

---

## 5. 配置文件 `config/config.yaml`
```yaml
# 关注范围（未来扩展只改这里）
focus:
  categories: ["AI 应用"]          # 后续可加 "Agent框架" "RAG" "多模态"
  search_topics: [ai, llm, agent, rag, llm-agent, ai-agent]
  min_stars: 200
  created_within_days: 30
  pushed_within_days: 7

collect:
  sources: [trending, search]       # 双源
  trending_since: [daily, weekly]
  top_n: 5                           # 每天深度学习的项目数

analyze:
  depth: medium                      # README + docs + release
  max_readme_chars: 12000

# 多模型可插拔：换模型只改这里（密钥/base_url 在 .env）
llm:
  provider: anthropic                # anthropic | openai | gemini | deepseek | openai_compatible | ollama
  model: claude-opus-4-8
  temperature: 0.3
  max_tokens: 4000
  fallback:                          # 主模型失败时按序降级（可留空）
    - { provider: deepseek, model: deepseek-chat }
    # - { provider: ollama,  model: qwen2.5 }

report:
  projects_dir: projects        # 项目库（与日期无关）
  daily_dir: daily              # 日报（按天）
  timezone: Asia/Shanghai

analyze_revisit:
  on_new_release: true          # 出新 release 则重学
  on_star_jump_pct: 30          # star 较上次增长 >=30% 则重学
  else_lightweight: true        # 否则只更新 metadata + history，不调 LLM

feishu:
  card_top_n: 5
  push_time: "08:00"
  # 接收者与密钥在 .env：FEISHU_APP_ID / FEISHU_APP_SECRET / FEISHU_RECEIVE_ID / FEISHU_RECEIVE_ID_TYPE

schedule:
  pipeline_time: "06:30"
  push_time: "08:00"
```
密钥走 `.env`，不进 config、不入库。

---

## 6. 技术栈

| 用途 | 选型 |
|---|---|
| 语言 | Python 3.11+ |
| HTTP | `requests` / `httpx` |
| HTML 解析（Trending） | `selectolax` 或 `beautifulsoup4` |
| GitHub | REST API（PAT 鉴权）+ Trending 抓取 |
| LLM | **多模型可插拔**：LiteLLM 统一适配（Anthropic/OpenAI/Gemini/DeepSeek/OpenAI 兼容/Ollama），config 切换 |
| 飞书 | 自建应用（tenant_access_token + `im/v1/messages` P2P 私聊发交互卡片） |
| 配置 | `pyyaml` + `python-dotenv` |
| 调度 | macOS `launchd`（plist） |

依赖少、可移植，未来迁服务器只换调度层（launchd → cron）。

---

## 7. 成本估算（粗略）

- GitHub API：带 PAT 完全在免费额度内
- Claude API：每天约 5~10 次调用（Top N=5，中档上下文）→ 量级很小，日成本可忽略到很低（取决于 README 长度）
- 飞书：免费
- 主要"成本"是首次开发工时

---

## 8. 异常处理与可靠性

| 风险 | 对策 |
|---|---|
| Trending 页面结构变动导致解析失败 | 解析失败时降级为只用 Search API，并告警 |
| GitHub 限流 | 必配 PAT；指数退避重试 |
| LLM 调用失败/超时 | 单项目失败不阻塞其他；记录失败、下次重试 |
| 学习未跑完就到 8:00 | 错峰设计 + push 只读已生成总览，发"已完成部分" |
| Mac 睡眠错过定时 | 文档提示保持唤醒；迁服务器彻底解决 |
| 飞书发送失败 | 重试 2 次 + 日志；可选系统通知降级 |
| 重复推送同一项目 | data/index.json 去重 + 复访判定 |

所有阶段统一写 `logs/<日期>.log`，便于回溯。

---

## 9. 渐进式落地里程碑

| 里程碑 | 内容 | 验收 |
|---|---|---|
| **M1 — 打通闭环（MVP）** | Search API 采集 → 单段 Claude 摘要 → 飞书发文本消息；手动运行 | 能在飞书收到一条当天 AI 项目简报 |
| **M2 — 双源 + 项目库** | 加 Trending 源、合并、项目库目录结构（projects/）、metadata.json | projects/ 下有以项目为单位的结构化目录 |
| **M3 — 中档深度报告 + 日报** | analysis.md / quickstart.md / README 快照 / history.md + daily/ 日报 + 飞书交互卡片 | 报告结构完整、日报引用项目库、卡片可跳转 |
| **M4 — 自动化 + 复访迭代** | launchd 错峰调度、index.json 去重、复访重学、连续上榜、异常处理 | 连续 3 天无人工干预稳定到货，老项目能原地迭代 |
| **M5（可选）** | 配置化扩展新类目；"感兴趣项目"手动触发深度源码分析 | 改 config 即可换关注方向 |

---

## 10. 未来扩展位

- **类目扩展**：`config.focus.categories` 增项即可（Agent 框架 / RAG / 多模态 / 具身智能…）
- **深度专题**：对某项目手动触发"源码级"深度分析（即原方案 B 的 Claude Code agent 用法）
- **多渠道推送**：飞书之外加邮件 / Telegram，复用 summary 数据
- **趋势分析**：基于历史 metadata 做"周/月热度趋势"二次报告
- **迁移服务器**：调度层 launchd → cron，保证 7×24 准时

---

## 附：待你确认/决策的开放项
1. ✅ GitHub PAT — 已提供，存入 `.env`
2. ✅ 飞书自建应用 App ID / Secret — 已提供，存入 `.env`
3. ⏳ **飞书推送目标（P2P 推给你本人）** — 需要你的 `open_id`（`ou_…`），或注册邮箱/手机。
   - 拿 `open_id` 三选一：① 开放平台「API 调试台」调一次拿到；② 给我邮箱/手机我用通讯录接口换；③ 你私聊机器人一句，从消息事件里取。
   - 另需在飞书开放平台开启 `im:message`、`im:message:send_as_bot`（如用邮箱/手机换 open_id 再加 `contact:user.base:readonly`）并**发布版本**。
4. ⏳ **LLM key** — 看你选哪个 provider（默认 Anthropic 则填 `ANTHROPIC_API_KEY`；用 DeepSeek 则填 `DEEPSEEK_API_KEY` 并把 config `llm.provider` 改为 `deepseek`）。你说晚些提供。
5. "每天 Top N" 默认 5，是否合适？
```
