## 安装
**推荐（零构建，v0.24+）**：
```bash
npx taiyi-forge-install --all          # 一键装到 Claude/Codex/Cursor/OpenCode
npx taiyi-forge-install --cursor       # 仅装到 Cursor
```
**未发布到 npm 时可从 GitHub 直装**：
```bash
npm install 'git+https://github.com/Dong90/oh-my-taiyiforge.git#v0.38.0'
npx -p 'git+https://github.com/Dong90/oh-my-taiyiforge.git#v0.38.0' taiyi-forge-install --all
```
**源码安装**：
```bash
git clone https://github.com/Dong90/oh-my-taiyiforge.git
cd oh-my-taiyiforge && npm install && npm run build && npm test
node scripts/taiyi-forge.sh install --all
```

## 最小可用示例
1. 启动一个新变更：
   ```bash
   npx taiyi walkthrough
   ```
   或在 AI 终端中直接说：
   ```
   /taiyi:new "优化登录流程"
   ```
2. 查看当前阶段及下一步：
   ```
   /taiyi:status
   ```
3. 编辑生成的 `CHANGE.md` 后，推进阶段（人类门控）：
   ```
   /taiyi:continue --approver "你的名字"
   ```
4. 继续编写当前阶段工件：
   ```
   /taiyi:write
   ```
5. 执行开发与测试：
   ```
   /taiyi:apply
   ```
6. 完成后提交并归档：
   ```
   /taiyi:commit
   /taiyi:archive
   ```

## 依赖前提
- Node.js >= 20
- 目标 AI 终端之一已安装（Claude Code、Codex、Cursor 或 OpenCode）
- 可选：Playwright（用于内置冒烟测试，运行 `/taiyi:test smoke` 时需要）