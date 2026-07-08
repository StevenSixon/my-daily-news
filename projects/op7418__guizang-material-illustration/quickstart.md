## 安装

前提：在 Claude Code 或 Codex 等 Agent 环境中运行，Agent 需要有 shell 执行权限和图像生成能力。

### 1. 安装 Skill

```bash
npx skills add https://github.com/op7418/guizang-material-illustration --skill guizang-material-illustration
```

或者直接把下面这段话发给 AI：

> 帮我安装 `guizang-material-illustration`。请把 https://github.com/op7418/guizang-material-illustration 克隆到 ~/.claude/skills/guizang-material-illustration，安装完成后检查 SKILL.md、assets/、references/ 是否存在。

### 2. 最小可用示例

安装后直接对 Agent 说：

```text
用歸藏的材质插画 skill，帮我把这段产品说明做成一张带中文标签的机制图。
```

其他典型请求：

- 文章挑 3 个核心概念，各生成一张带字配图。
- 把柱状图截图重画成歸藏材质风格，保留数据和坐标。
- 先查 PKCE 参考信息，再做流程图。
- 生成杠杆原理图，图中标出支点、用力点、阻力点。

### 3. 联动 Social Card Skill

先生成中心图，再让 Social Card Skill 排成 3:4 小红书卡片：

```text
先生成中心配图，再交给社交媒体卡片 Skill 排成 3:4 小红书卡片。
```