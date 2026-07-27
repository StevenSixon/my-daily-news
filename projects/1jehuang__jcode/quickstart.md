**安装**  
- macOS/Linux：`curl -fsSL https://jcode.sh/install | bash`  
- Windows：在PowerShell执行 `irm https://jcode.sh/install.ps1 | iex`  
- 也支持Homebrew或从源码编译（需Rust工具链）

**前置条件**  
- 需要配置至少一个LLM提供商的API密钥（如设置`ANTHROPIC_API_KEY`环境变量）；具体配置方法参照`https://jcode.sh/docs`（README未展开说明）

**最小可用**  
`jcode` 进入交互式TUI，输入问题即可开始对话。可创建多个会话，利用自动记忆功能跨会话关联上下文。