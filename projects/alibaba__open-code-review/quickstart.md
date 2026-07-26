**前提要求**
- Git >= 2.41
- Node.js环境（用于npm安装）

**安装**
```bash
npm install -g @alibaba-group/open-code-review
```
安装后`ocr`命令全局可用。

**快速体验**
```bash
# 1. 配置LLM（交互式）
ocr config provider   # 选择内置Provider或自定义
ocr config model      # 选择模型

# 2. 进入项目，审查当前工作区变更（staged+unstaged+untracked）
cd your-project
ocr review

# 3. 审查分支差异
ocr review --from main --to feature-branch

# 4. 全文件扫描（无需Git历史）
ocr scan --path internal/agent
```

**高级用法**
- 中断恢复：`ocr session list` 查看会话，然后用 `--resume <session-id>` 续审
- 代理模式：`ocr delegate preview` 让其他AI编码代理执行审查（无需配置LLM）
- 更多见官方文档：https://open-codereview.ai/docs