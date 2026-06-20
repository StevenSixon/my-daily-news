# AI 资讯并行轨 — 技术设计文档

> 在「AI 项目日报」之外，每天汇聚各大 AI 头部公司 / 平台的**一手资讯**（官方博客、论文、社区热点），与项目榜并行呈现于日报、看板与飞书推送。
>
> 总体项目设计见 [`DESIGN.md`](./DESIGN.md)；本文聚焦资讯轨。

---

## 1. 目标与范围

### 1.1 要解决的问题
项目榜（GitHub trending）只覆盖「开源项目」这一类信号。用户还需要追踪 **AI 头部公司与各大平台的最新一手消息**：模型发布、研究进展、产品更新、行业动态。

### 1.2 设计原则
- **并行轨，不污染项目模型**：资讯是「文章」（标题/链接/来源/发布时间/摘要），没有 star/streak/复访语义。绝不塞进项目 `items`，避免破坏现有排序与复访逻辑。
- **复用现有基建**：LLM（`llm_client`）、存储（`store`）、日报（`build_summary`）、推送（`push`）、看板（`gen-data.mjs` + React）全部复用。
- **来源可信优先**：只接**无反爬的公开 RSS / 公共 API**，且以一手官方源权重最高。
- **故障隔离**：资讯轨任何失败都不能影响项目日报的产出。
- **成本可控**：LLM 调用量由 `max_items` 封顶，且可一键关闭（降级为纯标题聚合）。

### 1.3 不做 / 暂不做
- ❌ 微信公众号（无开放 API，难自动化）。
- ❌ Medium 整站/按 tag 抓取（信噪比过低，详见调研结论）。
- ⏸️ Anthropic / Meta AI 官方 RSS：经多次探测，当前站点为 JS 渲染、无任何公开 feed（`/rss`、`/news.xml`、`/index.xml`、`/feed/` 等均 404），已在 config 中以注释占位，待官方提供后启用。
- ✅ Reddit：JSON API 被反爬封禁（403），已改用其 **RSS 端点**接入（见 §3.1）。
- ✅ 跨源 LLM 聚类去重（同一事件多源合并）：已实现（见 §3.2）。
- ✅ 周资讯回顾报告：已实现（见 §3.6）。

---

## 2. 总体架构

```
                    ┌──────────────── pipeline._run() ────────────────┐
项目轨：collect → analyze → (items, streaks) ─┐                        │
                                              ├─→ build_summary.build()│→ daily/<date>.json (+news)
资讯轨：news_collect → news_summary → (news) ─┘   ↘ daily/<date>.md      │       │
       （完全隔离在 _collect_news 的 try/except）                       │       ├─→ push.py    → 飞书卡片（含资讯段）
                                                                       │       └─→ gen-data.mjs → 看板「AI 资讯」tab
                                                                       └─────────────────────────────────────────┘
```

资讯轨两步：
1. **`news_collect.collect_news()`** — 抓取 → 时间窗过滤 → 按 URL 去重 → 社区源 AI 关键词过滤 → 返回候选。
2. **`news_summary.summarize()`** — 打分排序 → 截断 `max_items` → （可选）LLM 中文一句话摘要 + 分类。

产出的 `news` 列表作为**附加字段**写入 `daily/<date>.json`，下游三个输出面各自消费。

---

## 3. 模块详细设计

### 3.1 `src/news_collect.py` — 采集与去重
- **源类型**：
  - `official`（一手公司博客 RSS）— OpenAI、Google DeepMind、Google AI。
  - `paper`（论文 RSS）— arXiv cs.AI / cs.CL / cs.LG。
  - `hf`（Hugging Face Blog RSS）。
  - `community`（Hacker News，Algolia API）+ **Reddit**（r/LocalLLaMA、r/MachineLearning，走 RSS 端点，`ai_filter` 关键词过滤）。Reddit 对密集请求会 429，源间留 2s 延时。
- **RSS 抓取**：`requests` 取原文 → `feedparser` 解析。`bozo` 且无 entries 视为失败源，**安全跳过**（`log.warning`），不影响其余源。
- **时间窗**：只保留 `published`/`updated` 在 `window_days`（默认 3 天）内的条目，避免首跑回灌历史（如 OpenAI feed 有上千条历史）。无发布时间的条目丢弃。
- **Hacker News**：`search_by_date` + `numericFilters: points>=hn_min_points, created_at_i>cutoff`，再用 `_AI_RE` 关键词过滤标题（社区源才需要相关性过滤）。无外链的故事回退到 HN 讨论页。
- **去重**：
  - 批内：按 URL 合并多源命中同一链接。
  - 历史：`data/news-seen.json`（`{url: 首次见到日期}`）过滤已收录链接。
- **`mark_seen(items)`**：流水线采纳后回写 seen，并清理 30 天外旧记录控制体积。**仅标记已采纳条目**，落选候选可在窗口内重新竞争。

### 3.2 `src/news_summary.py` — 打分、配额、去重、摘要
处理流水线：**打分排序 → 来源配额 → LLM 加工 + 跨源去重 → 截断**。
- **打分** `_score`：`来源权重 + 时效加成 + HN 热度`
  - 来源权重 `_TYPE_WEIGHT`：official 100 / paper 70 / hf 70 / community 45。
  - 时效：当天 +25，按天线性衰减（约 3 天归零）。
  - HN 点赞：`min(points/8, 30)`，封顶以免压过一手源。
- **来源配额** `_apply_quota`（前置）：按 `news.type_quota` 丢弃超额来源类型（如 `paper: 4`、`community: 5`），防 arXiv 论文刷屏。**配额必须在构建 LLM 池之前施加**——否则池被单一来源占满，配额一砍就凑不满 `max_items`。
- **LLM 加工 + 去重** `_llm_enrich` / `_dedupe_by_event`：批量 prompt → 每条 `summary_zh`（≤40 字）+ `category` + **`event_key`**（事件英文标识，同一事件多源给相同 key）→ 按 `event_key` 跨源去重，保留得分更高的代表。LLM 池取 `max_items*2`（含去重余量），最后截断到 `max_items`。
- **降级**：`llm_summarize=false` 或 LLM 不可用 → 保留空摘要、不做去重，渲染层回退到原标题。

### 3.3 输出面 ①：日报 `build_summary.py`
- `build(items, streaks, news=...)`：`news` 写入 payload 的 **附加字段**；Markdown 末尾追加「📰 AI 资讯」段（`_render_news`，按来源类型加 emoji 🏢/📄/🤗/💬）。
- **向后兼容**：现有消费方（`push.py` 旧逻辑、`gen-data.mjs`）只读 `items`，新增 `news` 字段不破坏任何东西。

### 3.4 输出面 ②：飞书 `push.py`
- 在卡片中追加「📰 AI 资讯」段（`feishu.news_top_n` 控制条数），每条：来源类型 + 分类 + 中文摘要（链接）+ 来源/日期。
- 与项目段、霸榜段以 `hr` 分隔；无资讯时整段省略。

### 3.5 输出面 ③：看板 `dashboard/`
- `gen-data.mjs`：从 `daily/<date>.json` 的 `news` 映射为每期 `news` 数组。
- `data.ts`：`NewsItem` 类型；`Edition.news?`（可选，兼容旧期）。
- `App.tsx`：第三个 view tab「AI 资讯 · N」，按选定日期展示当期资讯；`NewsRow` 点击新标签打开原文；资讯视图隐藏项目专属筛选（语言/分类/排序）。

### 3.6 `src/news_trend.py` — 周资讯回顾（二次报告）
- 镜像 `trend.py`：聚合统计窗口内各日 `daily/<date>.json` 的 `news`（跨日按 URL 去重）→ 按分类分组（`_CAT_ORDER` 排序，组内按日期倒序）+ 来源分布统计。
- 纯函数 `aggregate(dailies, today, days)` 便于测试；产出 `trends/<date>-news-weekly.(md|json)`，`--push` 时推送飞书（无资讯则跳过推送）。
- 数据全部来自已落盘日报，**不再抓取/调 LLM**。
- **调度**：`deploy/run.sh` 的 `weekly` 阶段在 `src.trend` 之后追加 `src.news_trend`，复用既有 weekly launchd 定时任务。

---

## 4. 数据模型

### 4.1 `daily/<date>.json` 的 `news` 字段（流水线产出）
```jsonc
{
  "date": "2026-06-20",
  "count": 6,
  "items": [ /* 项目，不变 */ ],
  "streaks": [ /* 霸榜，不变 */ ],
  "news": [
    {
      "title": "New usage analytics and updated spend controls...",  // 原标题
      "url": "https://openai.com/index/...",
      "source": "OpenAI",
      "source_type": "official",      // official | paper | hf | community
      "published": "2026-06-18",
      "summary_zh": "OpenAI 为企业版推出用量分析与支出控制。",  // LLM 生成，可空
      "category": "产品"               // 模型发布/研究/产品/工程/融资·商业/观点/其他
    }
  ]
}
```

### 4.2 `data/news-seen.json`（去重状态）
```jsonc
{ "https://openai.com/index/...": "2026-06-20" }   // URL → 首次见到日期，保留 30 天
```

---

## 5. 配置 `config/config.yaml`
```yaml
news:
  enabled: true
  window_days: 3          # 只收近 N 天发布的资讯
  max_items: 12           # 每天进日报的资讯条数（控 LLM 成本）
  llm_summarize: true     # false=仅标题聚合（零 LLM 成本、无去重）
  hn_min_points: 80       # Hacker News 点赞门槛
  type_quota:             # 各来源类型进日报上限（防刷屏；未列出=不限量）
    paper: 4
    community: 5
  sources:
    official: [ {name, url}, ... ]   # OpenAI / DeepMind / Google AI
    paper:    [ {name, url}, ... ]   # arXiv cs.AI / cs.CL / cs.LG
    hf:       [ {name, url} ]        # HF Blog
    reddit:   [ {name, url}, ... ]   # r/LocalLLaMA / r/MachineLearning（RSS 端点）
  hacker_news: true

news_trend:               # 周资讯回顾报告
  window_days: 7
  top_n: 8                # 每个分类展示条数
```
新增源只改这里；新增源类型需在 `news_collect`/`news_summary` 同步权重与配额。

---

## 6. 成本与可靠性
- **LLM 成本**：每天约 `max_items`（≈12）次调用中的 1 个批量请求，远低于项目深度分析；`llm_summarize=false` 可归零。
- **网络**：全部公开 RSS / 公共 API，无 token、无反爬；单源失败仅 `warning` 跳过。
- **隔离**：`pipeline._collect_news()` 整体 `try/except`，资讯失败 → 返回 `[]`，项目日报照常产出。
- **依赖**：仅新增 `feedparser==6.0.11`（运行环境需 `pip install -r requirements.txt`）。

---

## 7. 落地里程碑 / 状态

| 阶段 | 内容 | 状态 |
|---|---|---|
| **Phase 1** | 采集（官方/论文/HF/HN）+ 去重 + LLM 摘要 + 日报 md/json | ✅ 已交付 |
| **Phase 3** | 看板「AI 资讯」tab | ✅ 已交付 |
| **Phase 2** | 飞书资讯卡（推送侧） | ✅ 已交付 |
| 增强 | Reddit 源、来源配额、跨源 LLM 聚类去重 | ✅ 已交付 |
| 二次报告 | 周资讯回顾 `news_trend`（含 weekly 调度） | ✅ 已交付 |
| 待定 | Anthropic/Meta RSS（无公开源）、Techmeme/工程博客、embedding 去重 | ⏸️ |

> 注：阶段编号沿用最初规划（看板先于推送落地），非执行先后。

---

## 8. 未来扩展位
- **Anthropic / Meta 官方 RSS**：待其提供公开 feed 后接入（当前无）。
- **更多源**：Techmeme、各公司工程博客、更多子版块。
- **embedding 去重**：当前跨源去重靠 LLM 给 `event_key`；后续可用向量相似度做更鲁棒的事件聚类。
- **资讯热度信号**：为非 HN 源引入更统一的热度度量（如 Reddit ups），优化排序。
