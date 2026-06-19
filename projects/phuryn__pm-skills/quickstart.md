## 安装

### 前置依赖
- Claude Cowork（推荐非开发者）或 Claude Code CLI（已安装Node.js）。
- 如需在其他AI助手上使用技能，需对应环境的技能文件夹访问权限（如Gemini CLI、OpenCode等）。

### 通过Claude Cowork安装（一键）
1. 打开Customize（左下角）
2. 进入 Browse plugins → Personal → +
3. 选择 “Add marketplace from GitHub”
4. 输入 `phuryn/pm-skills`，所有9个插件自动安装，同时获得命令和技能。

### 通过Claude Code CLI安装
```bash
# 添加市场
claude plugin marketplace add phuryn/pm-skills

# 安装所有插件（可选择性安装）
claude plugin install pm-toolkit@pm-skills
claude plugin install pm-product-strategy@pm-skills
claude plugin install pm-product-discovery@pm-skills
claude plugin install pm-market-research@pm-skills
claude plugin install pm-data-analytics@pm-skills
claude plugin install pm-marketing-growth@pm-skills
claude plugin install pm-go-to-market@pm-skills
claude plugin install pm-execution@pm-skills
claude plugin install pm-ai-shipping@pm-skills
```

### 最小可用示例
安装后在对话中直接使用命令：
```
/discover AI驱动的会议摘要工具，面向远程团队
```
系统将依次执行：生成创意 → 识别关键假设 → 按风险×影响排序 → 设计实验。

也可以单独调用技能，例如：
```
/strategy B2B项目管理SaaS
```
将输出完整的9模块产品策略画布。

技能可在自然语言中自动触发，如：
“帮我绘制我们产品功能的机会解决方案树（OST）”

### 其他AI助手上手指南
将技能文件夹复制到对应环境的技能目录：
```bash
# 示例：为OpenCode复制所有技能
for plugin in pm-*/; do
  mkdir -p .opencode/skills/
  cp -r "$plugin/skills/"* .opencode/skills/ 2>/dev/null
done
```
之后用自然语言描述工作流即可，斜杠命令仅Claude环境支持。