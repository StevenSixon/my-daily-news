## 安装
确保已安装 Node.js 和 `npx`。

安装全部技能（推荐）：
```bash
npx skills add https://github.com/Leonxlnx/taste-skill
```

安装单个技能（如默认设计技能）：
```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

## 使用
在 ChatGPT、Codex、Cursor 或 Claude Code 的对话中，只需提及技能名称或直接粘贴对应 `SKILL.md` 文件内容。

示例提示：
> 使用 taste-skill 帮我创建一个现代博客首页，设计方差设为8，动效强度6。

若需要 v1 稳定版：
```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend-v1"
```

## 依赖前提
- 任意支持自定义系统提示或文件附件的 AI 编码工具（Codex、Cursor、Claude Code 等）
- 如果要用图像生成技能，需配合 ChatGPT Images 或 Codex 图像模式