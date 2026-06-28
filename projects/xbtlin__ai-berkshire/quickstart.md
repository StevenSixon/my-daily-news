## 安装
```bash
# 1. 安装 Claude Code（需 Node.js）
npm install -g @anthropic-ai/claude-code

# 2. 克隆仓库并安装 Skills
git clone https://github.com/xbtlin/ai-berkshire.git
cd ai-berkshire
./scripts/install-claude-commands.sh
```

Codex 用户用 `./scripts/install-codex-skills.sh` 替代。

## 最小可用示例
在 Claude Code 终端直接输入：
```
/investment-research 腾讯
```
即可获得包含四大师评分、估值区间、操作建议的完整投研报告。

## 前提
- Claude Code 或 Codex 客户端已安装并配置 API 密钥
- 网络搜索功能可用（Agent 需要实时信息）
- 对价值投资基本概念有了解（能力圈、安全边际等）