## 安装
```bash
pip install vulnclaw
```
## 最小可用示例
1. 配置模型提供商
```bash
vulnclaw config provider deepseek   # 或其他兼容模型
vulnclaw config set llm.api_key sk-your-key
```
2. 运行环境检查
```bash
vulnclaw doctor
```
3. 启动交互式会话，对目标进行渗透测试
```bash
vulnclaw
# 进入 CLI 后输入：对 http://testphp.vulnweb.com 进行渗透测试
```
或使用单命令模式：
```bash
vulnclaw run http://testphp.vulnweb.com
```
## 依赖前提
- Python 3.10+
- Node.js（用于 MCP 服务）
- nmap（可选，用于端口扫描）