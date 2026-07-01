**安装**
```bash
npm install -g umadev
```
确保已安装并登录至少一个 AI 编码 CLI（任选）：
- Claude Code: `npm i -g @anthropic-ai/claude-code && claude auth login`
- Codex: `npm i -g @openai/codex && codex login`
- OpenCode: 见 opencode.ai, `opencode auth login`

**最小可用**
```bash
umadev          # 启动聊天界面，首次运行会要求选择基地
```
然后输入需求，例如：
```
> add CSV export to the reports page
```
或直接非交互式构建：
```bash
umadev run "add CSV export to the reports page" --backend claude-code
```
umadev 会自动规划并执行，输出文档、代码和交付物。所有构建在隔离分支完成，不干扰当前工作目录。

**若想从源码构建（可选）**
```bash
git clone https://github.com/umacloud/umadev.git
cd umadev && cargo build --release --features vector-local
./target/release/umadev --version
```
需要提前下载嵌入模型到 `~/.umadev/embed-model/`，否则仅退化为 BM25 检索。