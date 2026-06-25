## 安装

### 前提
- Node.js 环境（安装 Claude Code 需要 npm）
- Anthropic Claude Code 订阅（需能使用 Claude 模型）

### 步骤

```bash
# 1. 安装 Claude Code（全局）
npm install -g @anthropic-ai/claude-code

# 2. 克隆 AI Berkshire 仓库
git clone https://github.com/xbtlin/ai-berkshire.git

# 3. 将 skill 文件复制到 Claude Code 的命令目录
cp ai-berkshire/skills/*.md ~/.claude/commands/
```

### 最小可用示例

启动 Claude Code 后，直接输入 `/investment-research 腾讯` 即可开始对腾讯的四大师综合深度研究。

其他示例：
```bash
# 4 Agent 并行快速研究
/investment-team 美团

# 巴菲特六关快速筛选
/investment-checklist 茅台, 英伟达, 苹果

# 研究未上市公司
/private-company-research SpaceX

# 股价异动快速归因
/news-pulse 腾讯
```

注意：所有研究均依赖 Claude Code 的实时联网搜索能力，确保数据来自最新公开信息。