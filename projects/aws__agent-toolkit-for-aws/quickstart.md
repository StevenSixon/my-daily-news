## 快速上手
### Claude Code（推荐）
```
/plugin install aws-core@claude-plugins-official
```
如提示未找到，先更新市场：
```
/plugin marketplace update claude-plugins-official
```
### Codex
```
codex plugin marketplace add aws/agent-toolkit-for-aws
# 在 Codex 中运行 /plugins，安装 aws-core
```
### Cursor
在 Settings → Plugins → Team Marketplaces → Add Marketplace → Import from Repo，填入 `aws/agent-toolkit-for-aws`，然后在插件面板安装 aws-core。

### 其他代理（通用方式）
1. 安装 [uv](https://docs.astral.sh/uv/)
2. 在代理的 MCP 配置中添加服务器：
```json
{
  "mcpServers": {
    "aws": {
      "command": "uvx",
      "args": ["mcp-proxy-for-aws@1.6.3", "https://aws-mcp.us-east-1.api.aws/mcp", "--metadata", "AWS_REGION=us-west-2"]
    }
  }
}
```
3. 安装技能：
```
npx skills add aws/agent-toolkit-for-aws/skills
```

**前提**：本地已配置 AWS 账号凭证（API 调用需要），节点环境支持 `npx`。