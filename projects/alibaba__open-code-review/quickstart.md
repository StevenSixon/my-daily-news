**1. 前提**：Git >= 2.41
**2. 安装**：`npm install -g @alibaba-group/open-code-review` 
**3. 配置模型**：`ocr config provider` 交互式选择提供商并设置API密钥
**4. 审查**：
```bash
cd your-project
ocr review                   # 审查所有暂存及其它改动
ocr review --from main --to feature  # 分支对比
ocr scan                     # 全仓库文件审查
```
**5. 更多**：查看帮助 `ocr --help`，官方文档 [open-codereview.ai/docs](https://open-codereview.ai/docs)