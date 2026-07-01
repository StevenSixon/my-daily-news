## 安装
### OpenCode用户（推荐）
在OpenCode聊天框发送以下提示词，AI自动安装：
```
请调研 https://github.com/hoolulu/deep-research 项目，按照文档要求依次完成：
1. 安装前置依赖（根据Scrapling官方文档和你的操作系统）
2. 注册Scrapling MCP Server，确保重启后正常使用
3. 注册 /research 和 /research-update 命令
每完成一步确认结果，完成后读取VERSION确认版本号。
```
### 非OpenCode用户（Claude Code/Cursor/Codex CLI等）
粘贴以下提示词到工具中，AI会适配安装：
```
请调研 https://github.com/hoolulu/deep-research 项目，自动安装前置依赖并改造适配当前CLI工具：
1. 安装Python和Scrapling（参考官方文档和系统）
2. 注册Scrapling MCP Server
3. 根据当前工具注册 /research 和 /research-update 等价入口
4. 将多agent链式架构翻译为当前工具的等价实现
5. 若本机有多个CLI工具，只配置当前工具
每完成一步确认结果。
```
### 依赖
- LLM运行时：OpenCode、Claude Code、Cursor等任一
- 在线模式：Scrapling（Python库）；离线模式无需
- 搜索：使用作者部署的SearXNG，零配置

## 最小可用示例
安装重启后在聊天框输入：
```
/research 中国新能源汽车产业发展现状 -quick
```
约8-12分钟后，在 `~/.opencode/skills/deep-research/reports/` 得到Markdown报告，用浏览器打开 `reports-browser/index.html` 可预览。支持命令：
- `/research 主题`        # standard 模式
- `/research 主题 -deep`  # 深度模式
- `本地资料调研`         # 指定文件夹生成报告（见FAQ）
- `/research-update`     # 检查更新