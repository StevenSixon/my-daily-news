## 安装

**前提条件**：Node.js ≥ 18

### 一键安装（macOS / Linux / WSL / Git Bash）

```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash
```

### Windows（PowerShell 5.1+）

```powershell
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex
```

安装过程约 30 秒，会自动检测已安装的代理并注入技能文件。已有代理未检测到可忽略，重新运行不会重复安装。

## 最小可用示例

1. 在任意支持的代理（Claude Code、Cursor、Codex 等）对话中输入：

   ```
   /caveman
   ```

   或自然语言：“talk like caveman”。

2. 之后所有回复将被压缩，例如：

   > **原来**：“The reason your React component is re-rendering is likely because you're creating a new object reference on each render cycle. When you pass an inline object as a prop, React's shallow comparison sees it as a different object every time, which triggers a re-render. I'd recommend using useMemo to memoize the object.”（69 token）
   > 
   > **压缩后**：“New object ref each render. Inline object prop = new ref = re-render. Wrap in `useMemo`.”（19 token）

3. 恢复正常模式：

   ```
   normal mode
   ```

## 进阶用法

- 切换压缩等级：`/caveman ultra`
- 查看节省统计：`/caveman-stats`
- 压缩记忆文件：`/caveman-compress CLAUDE.md`
- 生成提交信息：`/caveman-commit`