## 安装
1. 克隆仓库：`git clone https://github.com/dzcmemory-web/bazi-ziwei-skill.git`
2. 进入算法目录安装依赖：`cd bazi-ziwei-skill/calculator && npm install` （需要 Node.js >= 18）
3. 将整个文件夹放入 Agent 的 skills 目录（各 Agent 路径见 README）

## 最小可用示例
对 Agent 说：
> 我是 2000 年 1 月 1 日中午 12 点出生的男生，帮我看下命盘。

Agent 会引导选择分析模式，然后自动排盘并输出结果。

也可命令行直接排盘：
```bash
cd calculator
node dist/run-chart.js --year=2000 --month=1 --day=1 --hour=12 --minute=0 --gender=male > chart.json
node dist/dump-text.js --input=chart.json --output=chart.txt
```
## 生成海报
```bash
node dist/render.js --chart=chart.json --analysis=analysis.json --template=../templates/report-zonghe-poster.html --output=report.html --currentYear=2026
```