## 安装方式

### 前提
- Node.js ≥ 20
- 任一目标 AI 终端：Claude Code、Codex、Cursor 或 OpenCode

### 一行安装（推荐）
```bash
npx taiyi-forge-install --all   # 自动安装到所有已检测到的 AI 终端
npx taiyi-forge-install --cursor # 仅安装到 Cursor
```

### 源码安装（可选）
```bash
git clone https://github.com/Dong90/oh-my-taiyiforge.git
cd oh-my-taiyiforge
npm install && npm run build && npm test
node scripts/taiyi-forge.sh install --all
```

### 从 GitHub 直接安装（npm 未发布时）
```bash
npm install 'git+https://github.com/Dong90/oh-my-taiyiforge.git#v0.28.1'
```

## 最小可用示例

### 第一个变更
```bash
npx taiyi new "优化登录流程"    # 自动创建 .taiyi/changes/<slug>/CHANGE.md
npx taiyi status                 # 查看当前阶段及下一步建议
# 编辑 CHANGE.md，然后人类确认
npx taiyi complete <slug> change --approver "你的名字"
# 后续阶段由引擎自动推进或通过聊天斜杠继续
```

### 聊天斜杠命令（在 AI 终端中输入）
```
/taiyi:new "功能描述"           # 初始化变更
/taiyi:status                    # 查看阶段状态和推荐动作
/taiyi:write                     # 编写当前阶段工件
/taiyi:continue --approver "名字" # 通过人工审批后继续
/taiyi:apply                     # 执行 dev/test 检查清单
/taiyi:archive                   # 九阶段全部完成后归档
```

### 常用巡检
```
/taiyi:doctor                    # 安装与工作区自检
/taiyi:test smoke                # Playwright 内置冒烟测试
/taiyi:token compress <slug>     # 精简上下文，防止会话超长
```