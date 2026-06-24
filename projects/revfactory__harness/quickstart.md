## 安装前提
- 拥有 Claude Code 环境，且支持 Plugin 系统（需能运行 `/plugin` 命令）
- （可选）若采用直接安装方式，需有文件系统写入权限

## 通过 Marketplace 安装（推荐）
```shell
# 添加 marketplace
/plugin marketplace add revfactory/harness

# 安装插件
/plugin install harness@harness-marketplace
```

## 直接安装为全局 Skill
```shell
# 将技能目录复制到 Claude Code 技能文件夹
cp -r skills/harness ~/.claude/skills/harness
```

## 最小可用示例
1. 在 Claude Code 交互界面输入以下提示之一：
   - `Build a harness for this project`
   - `Design an agent team for this domain`
   - `Set up a harness`
2. Claude Code 自动执行 6 阶段分析，并生成如下目录结构：
```
your-project/
├── .claude/
│   ├── agents/          # Agent 定义文件
│   │   ├── analyst.md
│   │   ├── builder.md
│   │   └── qa.md
│   └── skills/          # 技能文件
│       ├── analyze/
│       │   └── SKILL.md
│       └── build/
│           ├── SKILL.md
│           └── references/
```
3. 即可在后续对话中通过 `/task` 或直接调用 Agent 名使用生成的团队。

## 执行模式选择
- **Agent Teams**（默认）：适用于需要 2 个以上 Agent 协作的任务，内部使用 TeamCreate + SendMessage + TaskCreate
- **Subagents**：适用于一次性任务、无需 Agent 间通信的场景，直接调用 Agent 工具