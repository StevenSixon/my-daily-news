# AI 项目日报助理

每天自动发现 GitHub 上爆火的 **AI 应用类**项目，深度学习并归档到本地，每天早上 8:00 通过**飞书机器人私聊**推送简短汇报。

> 完整设计见 [`docs/DESIGN.md`](docs/DESIGN.md)。

## 特性
- **双数据源**：GitHub Trending + Search API，合并去重，LLM 过滤出「AI 应用」
- **项目库 / 日报分离**：`projects/`（按项目持续迭代，与日期无关）+ `daily/`（按天）
- **多模型可插拔**：Anthropic / OpenAI / Gemini / DeepSeek / OpenAI 兼容 / Ollama，改配置即切换，支持失败降级
- **复访迭代**：老项目再上榜时，有新 release / star 大涨才重学，否则只更新元数据，省成本
- **飞书私聊推送**：自建应用，交互卡片，08:00 定时

## 目录结构
```
projects/<owner__repo>/   # 项目库：metadata.json / analysis.md / quickstart.md / history.md / README.snapshot.md
daily/<date>.md|.json     # 日报（json 供推送用）
data/index.json           # 全局索引 + 去重 + 复访判定
src/                      # 代码
config/config.yaml        # 配置（关注范围、top_n、llm、飞书）
deploy/                   # launchd plist + run.sh
```

## 快速开始
```bash
# 1) 依赖
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2) 配置密钥
cp .env.example .env      # 然后填入 GITHUB_TOKEN / FEISHU_* / 选定 provider 的 LLM key

# 3) 跑一次完整流水线（采集 + 学习 + 生成日报）
python -m src.pipeline

# 4) 推送当天日报到飞书
python -m src.push

# 单独调试某一步
python -m src.collect          # 只看采集结果
```

## 配置要点（`config/config.yaml`）
- `focus.search_topics` / `min_stars`：关注范围，未来扩展类目改这里
- `collect.top_n`：每天最多深度学习的项目数（默认 5）
- `llm.provider` / `llm.model`：换模型只改这两行；密钥放 `.env`
- `analyze_revisit`：老项目何时重学

## 必填密钥（`.env`）
| 变量 | 说明 |
|---|---|
| `GITHUB_TOKEN` | GitHub PAT（只读 public 即可） |
| `FEISHU_APP_ID` / `FEISHU_APP_SECRET` | 飞书自建应用 |
| `FEISHU_RECEIVE_ID` / `FEISHU_RECEIVE_ID_TYPE` | 推送给你本人：`open_id`(ou_...) 或 email/mobile |
| 选定 provider 的 key | 如 `ANTHROPIC_API_KEY` / `DEEPSEEK_API_KEY` … |

飞书后台需开启权限 `im:message`、`im:message:send_as_bot`（用邮箱/手机定位再加 `contact:user.base:readonly`）并**发布应用版本**。

## 部署（launchd，macOS）
```bash
# 1) 把 plist 里的 PROJECT_DIR 占位符替换为本项目绝对路径
PROJECT_DIR="$(pwd)"
sed "s#PROJECT_DIR#${PROJECT_DIR}#g" deploy/com.daily-news.pipeline.plist > ~/Library/LaunchAgents/com.daily-news.pipeline.plist
sed "s#PROJECT_DIR#${PROJECT_DIR}#g" deploy/com.daily-news.push.plist     > ~/Library/LaunchAgents/com.daily-news.push.plist
chmod +x deploy/run.sh

# 2) 加载
launchctl load ~/Library/LaunchAgents/com.daily-news.pipeline.plist
launchctl load ~/Library/LaunchAgents/com.daily-news.push.plist
```
- 06:30 跑流水线、08:00 推送（错峰，保证准时）
- Mac 睡眠会延迟触发；需保持唤醒/插电，或后续迁服务器用 cron

## 落地里程碑
M1 闭环 → M2 双源+项目库 → M3 深度报告+日报 → M4 自动化+复访迭代。详见设计文档。
