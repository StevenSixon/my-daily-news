## 安装
### 方式一：一行命令（推荐）
```bash
npx skills add alchaincyf/zhangxuefeng-skill
```
该命令自动检测当前runtime（Claude Code/Codex/Cursor等）并安装到正确目录。

### 方式二：手动安装
```bash
git clone https://github.com/alchaincyf/zhangxuefeng-skill ~/.claude/skills/zhangxuefeng-skill/
```
其他runtime路径见README。

### 方式三：作为参考资料
将`SKILL.md`内容直接粘贴到AI对话中。

## 使用
告诉你的agent：
```
> 用张雪峰的视角帮我分析这个专业选择
> 切换张雪峰，我孩子要填志愿了
```

## 依赖前提
- 任意支持Agent Skills的AI runtime（50+种可选）
- 无需额外模型密钥或API配置
- Skill不绑定特定底座模型，由runtime自行调度