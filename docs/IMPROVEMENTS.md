# 优化路线 & 改进清单

> 版本：v1　|　创建：2026-06-19　|　状态：待排期
> 基于对 v1 全量代码 + 实际产出数据的评审，对照同类「内容聚合 + LLM 摘要 + 定时推送」管道的最佳实践，列出已知不足与改进项。
> 配合阅读：[`DESIGN.md`](DESIGN.md)（系统设计）。

---

## 0. 现状评价（做得好的部分，改造时不要丢）

- **职责分层正确**：采集/推送 = 确定性脚本，只有「学习」调 LLM。不让 LLM 干抓取/发消息这类又贵又不稳的脏活。
- **知识库 / 时间线解耦**：`projects/`（按项目持续迭代）vs `daily/`（按天），长期沉淀知识资产。
- **错峰调度**：06:30 学、08:00 推 + JSON 侧车给 push 读，保证准时。
- **多模型抽象 + 降级链**、**复访判定省成本**、**飞书 token 缓存**、**JSON 容错修复**——已有生产细节意识。

> 改造原则：以上四点是地基，任何重构都应保留这些边界，不要把 LLM 调用渗进采集/推送层。

---

## 优先级总览

| 优先级 | 编号 | 改进项 | 影响 | 改动量 |
|---|---|---|---|---|
| ✅ **P0** | I-1 | 分类误判修复（iptv 案例）+ 关键词词边界 + reason 落盘 | 产品对错 | 小 |
| ✅ **P0** | I-2 | 修 Search 源 `stars_gained=0` 排序偏差 | 产品对错 | 小 |
| ✅ **P0** | I-3 | 失败告警（pipeline 崩了也要推一条，别静默） | 产品对错 | 小 |
| ✅ **P1** | I-4 | GitHub 请求加退避重试 + 复用 session | 可靠性 | 小 |
| ✅ **P1** | I-5 | 修复访逻辑割裂（`on_new_release` 当前失效） | 可靠性 | 中 |
| ✅ **P1** | I-6 | `index.json` 原子写入 | 可靠性 | 小 |
| ✅ **P2** | I-7 | 解析/分类/JSON 工具函数补单测 + Trending HTML fixture | 工程化 | 中 |
| ✅ **P2** | I-8 | 锁依赖版本 + 最简 CI | 工程化 | 小 |
| ✅ **P2** | I-9 | 杂项：`.gitignore` 去重、token 文件权限、repo 膨胀 | 卫生 | 小 |
| **P3** | I-10 | 并发 analyze + 合并 GitHub API 调用 | 性能 | 中 |
| **P3** | I-11 | 产品体验：推送理由、个性化、趋势报告、多渠道、质量自检 | 体验 | 大 |

---

## P0 — 直接影响产品对错

### I-1　分类准确率：存在真实 false positive　✅ 已完成（2026-06-19）
**问题**
- 实际数据里 `iptv-org/iptv`（12.5 万 star 的电视频道列表）被收录为「AI 应用」，是明确误判。
- 成因之一：`collect.py:_classify_ai_llm` 末尾的关键词兜底用 `setdefault`，LLM 漏判的会被关键词捞回。
- 成因之二：`_classify_ai_keyword` 用**子串匹配**（`"ai" in text`），会误命中 `hawaii`、`chair` 等。
- 分类 `reason` 算出来了但**没存进 metadata**，无法回看误判、迭代 prompt。

**改进**
- [x] 关键词兜底改**整词匹配**：预编译 `_KW_RE`（`\b{kw}\b`），前缀词（`fine-tun`）单列只卡左边界。已验证 `hawaii/air/storage/iptv` 不再误命中。
- [x] 把分类 `keep / category / reason` **落盘** `data/classify-log.jsonl`（含被丢弃项），并写入 `metadata.json` 的 `classify_reason`。
- [x] 加**手动 blocklist**：`config.focus.blocklist`，已 seed `iptv-org/iptv`，collect 阶段早过滤。
- [ ] （可选）飞书卡片加「这个不相关」反馈入口，把反馈写回 blocklist。

**涉及**：`src/collect.py`、`src/analyze.py`、`src/store.py`、`config/config.yaml`

---

### I-2　排序对 Search 源不公平　✅ 已完成（2026-06-19）
**问题**
- `github_client.search()` 里 `stars_gained = 0` 写死（Search API 无周增长）。
- 而 `collect()` 最终**按 `stars_gained` 排序** → 纯 Search 来源、未在 Trending 出现的项目增量恒为 0，几乎不可能进 Top 5。**双源里 Search 这一源被废了一半。**

**改进**
- [x] 新增 `_rank_score(item, index)` 作为排序键：① trending 有真实窗口增量则用之；② 否则用 `index.last_stars_total` 算自上次的真实增量；③ 全新项目用 `created_at` 起的**日均增速**（star/天）兜底。
- [x] `github_client.search()` 补 `created_at` 字段，`absorb()` 合并时补全。
- [x] 已验证：Search 源项目（`+0⭐`）现在得到非零 score 并与 trending 正常交织排序。

**涉及**：`src/collect.py`、`src/github_client.py`

---

### I-3　失败是静默的（最危险的可靠性盲区）　✅ 已完成（2026-06-19）
**问题**
- 若 06:30 的 pipeline 整体崩了，08:00 的 `push.py` 找不到当天 JSON 就 `sys.exit(1)`，**用户收不到任何东西、也不知道挂了**——无声失败 = 以为今天没新项目。

**改进**
- [x] 新增 `feishu_client.send_alert(title, lines, color)` 通用红色告警卡片。
- [x] `pipeline.run()` 拆为 `run`（try/except 包壳）+ `_run`（原逻辑），失败时推「采集失败 + 错误摘要」并 re-raise（保留 launchd 非零退出）。告警自身失败不掩盖原异常。
- [x] `push.py` 找不到 JSON 时推「今日无数据 / 上游可能失败」再退出。
- [ ] （可选）加「连续 N 天无产出」自检告警。

**涉及**：`src/pipeline.py`、`src/push.py`、`src/feishu_client.py`

---

## P1 — 可靠性

### I-4　GitHub 请求无重试/退避（与 DESIGN §8 承诺不符）　✅ 已完成（2026-06-19）
**问题**
- DESIGN §8 写了「GitHub 限流 → 指数退避重试」，但 `github_client.py` 全是裸 `requests.get` + `raise_for_status()`，无任何重试。
- Trending 抓取还绕过了 `self.session`（没带 token、没复用连接池）。

**改进**
- [x] `session` 挂 `urllib3.Retry`（total=3、backoff_factor=1.0 → 0/2/4s、429+5xx、`respect_retry_after_header=True`），mount 到 http(s)。
- [x] Trending 改走 `self.session.get`，统一连接复用 + 共享退避。
- [x] `respect_retry_after_header=True` 已尊重 `Retry-After`。（剩余额度的主动观测可后续按需加。）

**涉及**：`src/github_client.py`

---

### I-5　复访判定逻辑被割裂（`on_new_release` 当前失效）　✅ 已完成（2026-06-19）
**问题**
- `collect._decide()` 自己注释「复访需要 release 信息 → 在 analyze 阶段处理，这里用 star 增长粗判」。
- 但 `pipeline.run()` **只把 `decision in ("new","revisit")` 的喂给 analyze**。于是「出了新 release 但 star 没涨 30%」的老项目，在 collect 阶段被判 `skip_lightweight`，**到不了 analyze**，`analyze_revisit.on_new_release: true` 形同虚设。

**改进（采用方案 B，无重复抓 release）**
- [x] `pipeline._run` 把**所有老项目**（revisit + skip_lightweight）都送进 `analyze.learn`，由其权威的 `_should_revisit`（含 release 判定）最终裁决；新项目仍受 `top_n` 限制控成本。
- [x] `analyze.learn` 返回新增 `refreshed` 标志；日报**只收 new + 实际刷新**的老项目，未变动项目仅静默更新 streak/metadata，不刷屏。
- [x] 用 stub 单测验证：被 collect 判 `skip_lightweight` 但有新 release 的项目，仍能进 analyze 刷新并进日报。

**涉及**：`src/pipeline.py`、`src/analyze.py`

---

### I-6　`index.json` 非原子写入　✅ 已完成（2026-06-19）
**问题**
- `store.write_json` 直接覆写。写 `index.json` 时进程被杀会损坏索引，影响去重。

**改进**
- [x] 新增 `_atomic_write_text`（`tempfile.mkstemp` + `os.replace`），`save_index` 与 `write_json` 均改为原子写入，异常时清理临时文件。
- [ ] （可选）写前备份上一版 `index.json.bak`。

**涉及**：`src/store.py`

---

## P2 — 工程化

### I-7　零测试　✅ 已完成（2026-06-19）
**问题**：无任何测试。Trending HTML 解析是 DESIGN 自列的头号风险（GitHub 改版必挂），却无任何防护。

**改进**
- [x] 新增 `tests/`（pytest，`pytest.ini` + `requirements-dev.txt`），共 **42 个用例**：
  - `test_utils.py`：`parse_int` / `repo_slug`
  - `test_classify.py`：关键词整词匹配回归（hawaii/air/storage/iptv 不误命中）
  - `test_rank_score.py`：`_rank_score`（trending/历史增量/速度兜底/异常日期）
  - `test_json_repair.py`：`_strip_fences` / `_find_json_block` / `_try_parse_json`
  - `test_store_atomic.py`：原子写入 + jsonl 追加
  - `test_trending_parse.py`：真实裁剪 fixture（`tests/fixtures/trending_daily.html`）回归
- [x] **顺带修复**：测试暴露 `_find_json_block` 对「前置说明 + 围栏 JSON」解析不全，改为
  **括号配对扫描**（跳过字符串内引号），可丢弃前后多余内容；`chat()` 的 JSON 路径同样受益。

**涉及**：新增 `tests/`、`pytest.ini`、`requirements-dev.txt`；改进 `src/llm_client.py`

---

### I-8　依赖未锁定 + 无 CI　✅ 已完成（2026-06-19）
**问题**：`requirements.txt` 只用 `>=`（`litellm` 迭代极快，易破坏）。

**改进**
- [x] `requirements.txt` 直接依赖全部 `==` 锁到已验证版本（requests 2.34.1 / bs4 4.15.0 / PyYAML 6.0.3 / python-dotenv 1.2.2 / litellm 1.89.2）；`requirements-dev.txt` 锁 `pytest==9.1.1`。
- [x] `.github/workflows/ci.yml`：push(main) + PR 触发，Python 3.12 + pip 缓存，装 `requirements-dev.txt` 后跑 `pytest`。
- [ ] （可选）后续加 ruff lint、多版本矩阵、transitive 全量 lock（pip-tools/uv）。

**涉及**：`requirements.txt`、`requirements-dev.txt`、`.github/workflows/ci.yml`

---

### I-9　卫生类小瑕疵　✅ 已完成（2026-06-19）
- [x] `.gitignore` 里 `.env` 那段**重复粘贴了两次**，已去重；并补 `.playwright-cli/`、`.pytest_cache/`。
- [x] 飞书 token 缓存写入后 `os.chmod(..., 0o600)`，收紧为仅本人可读写。
- [ ] 评估 `daily/*`、`projects/*` 入库策略：作为个人知识资产可入库，但需意识到 repo 会随时间膨胀，必要时分库或加归档。（暂保留现状）

---

## P3 — 性能与产品体验（量大后再做）

### I-10　并发与 API 合并
- analyze 对 Top N 项目**串行**（每个 1~2 次 LLM + 多次 GitHub API）。量小无碍，`top_n` 调大或加类目后会慢。
- [ ] 用 `concurrent.futures` 并发处理项目。
- [ ] 合并单项目的多次 GitHub API（repo / readme / release / list_dir）。

### I-11　产品体验
| 方向 | 现状 | 改进 |
|---|---|---|
| 推送形态 | 名称 + 一句话 + star | 加「为什么值得看」一句理由 + 标签；卡片按钮直达 GitHub/本地报告 |
| 去噪 | 只过滤是否 AI | 个性化兴趣权重、已读/已忽略状态 |
| 趋势 | `metadata.appearances[]` 时间序列已存但没人用 | 「周/月热度榜」「谁在持续涨」二次报告（见 DESIGN §10） |
| 多渠道 | 仅飞书 | summary 已结构化，加邮件/Telegram 近乎零成本 |
| 质量评估 | LLM 报告无校验 | 轻量「自检 prompt」或抽样人工评分，防幻觉/空洞 |

---

## 变更记录
- 2026-06-19：初版，基于 v1 全量代码评审整理。
- 2026-06-19：完成 P0 三项（I-1 分类误判 / I-2 排序偏差 / I-3 失败告警），端到端验证通过。
- 2026-06-19：完成 P1 三项（I-4 退避重试+session / I-5 复访逻辑割裂 / I-6 index 原子写入），单测+契约验证通过。
- 2026-06-19：完成 I-9 卫生项 + I-7 测试套件（42 用例，pytest），并修复测试暴露的 `_find_json_block` 解析缺陷。
- 2026-06-19：完成 I-8（依赖 == 锁定 + GitHub Actions CI）。P0~P2 全部完成，仅余 P3。
