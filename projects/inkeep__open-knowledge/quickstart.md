### 安装与使用
**macOS**  
下载最新的 `.dmg` 文件，拖入 Applications 启动即可。

**Linux/Windows/Intel Mac**  
```bash
# 前置依赖：Node.js 24+
npm install -g @inkeep/open-knowledge

# 进入任意项目目录（或新建）
cd my-knowledge
ok init          # 初始化项目，自动配置 Claude/Codex 等代理的 MCP 技能
ok start --open  # 启动 Web 编辑器并在浏览器中打开
```

**最小可用示例**  
创建一篇 Markdown 笔记，选中一段文字，点击“Ask AI”，打开的终端中的 Claude/Codex 就会收到你的上下文，开始基于你的知识库回答问题或生成内容。