## 安装

1. 确保已安装：
   - Claude Code CLI
   - Python ≥ 3.10
   - Bun
   - LaTeX 环境（TeX Live / MacTeX / MiKTeX 等，需支持 lualatex 和 xelatex）
   - （可选）poppler-utils（用于 PDF 文本提取，ATS 检查用）

2. Fork 并克隆仓库：
   ```bash
   gh repo fork MadsLorentzen/ai-job-search --clone
   cd ai-job-search
   ```

3. 安装岗位搜索工具依赖：
   ```bash
   cd .agents/skills/jobbank-search/cli && bun install && cd ../../../..
   # 重复类似命令以安装其他 portal (jobdanmark-search, jobindex-search, jobnet-search, linkedin-search)
   ```

## 最小可用示例

1. 启动 Claude Code：
   ```bash
   claude
   ```

2. 运行初始化命令，建立你的个人画像：
   ```
   /setup
   ```
   （按提示选择从已有文档导入、粘贴简历或进行采访式输入）

3. 搜索岗位：
   ```
   /scrape
   ```
   系统会列出匹配的岗位，并显示匹配度评分。

4. 选择一个岗位生成申请材料：
   ```
   /apply <岗位URL或直接粘贴职位描述>
   ```
   代理将自动评估匹配度、生成定制 LaTeX 简历和求职信，并经审阅后输出最终文件。

5. 后续可定期使用 `/upskill`、`/expand`、`/interview`、`/outcome` 管理整个求职周期。

**自定义重要提示**：若你在非丹麦市场求职，请尽早运行 `/add-portal` 来为你当地的求职网站生成搜索模块，或直接使用 `/apply` 粘贴职位描述而跳过自动搜索。