### 前提
- 安装 Node.js 与 npm
- 拥有 Anthropic Claude Code 访问权限（需相应订阅或 API 额度）
- 基本的命令行操作能力

### 安装
```bash
# 克隆仓库
git clone https://github.com/xbtlin/ai-berkshire.git

# 复制所有 Skill 文件到 Claude Code 全局命令目录
cp ai-berkshire/skills/*.md ~/.claude/commands/
```

### 最小可用示例
在 Claude Code 交互界面中执行：
```bash
/investment-research 腾讯
```
系统将按七模块顺序生成四大师综合深度报告，包含生意本质、护城河、逆向思考、管理层评估、文明趋势、估值及决策备忘录，并输出明确的通过/不通过/灰色地带结论与建议价格区间。

其他高频用法：
```bash
/investment-team 美团          # 4 个 Agent 并行研究
/investment-checklist 茅台,苹果 # 六关快速筛选
/industry-research 核电        # 产业链全景扫描
/earnings-review 腾讯 2025Q4   # 一手财报精读
/portfolio-review              # 现有持仓诊断
```
更多 Skill 及详细用法见仓库 README。