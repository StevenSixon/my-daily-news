## 上手只需 3 步

1. **创建技能文件夹**
   ```bash
   mkdir my-first-skill
   cd my-first-skill
   ```

2. **编写 `SKILL.md`**  
   （具体元数据字段和格式请参阅官方规格 https://agentskills.io/specification）
   最小示例（假设元数据采用 YAML front matter）：
   ```markdown
   ---
   name: my-first-skill
   description: 演示技能，向用户问好并生成今日待办
   ---
   # 问候与待办生成
   1. 用用户的名字打招呼。
   2. 询问今天最重要的 3 件事。
   3. 生成 Markdown 格式的待办清单。
   ```

3. **在支持的客户端中使用**  
   将整个 `my-first-skill/` 放入 Agent 客户端的技能目录，或通过配置指向它。启动后，Agent 会读取所有技能的摘要，当任务匹配"问好并生成待办"时自动加载该技能。

**依赖前提**：任何实现了 Agent Skills 规范的 AI 客户端（见 https://agentskills.io/clients ），无需安装额外工具。