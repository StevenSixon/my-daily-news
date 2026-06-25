### 安装
```bash
# 方式1：npx（推荐）
npx skills add mukul975/Anthropic-Cybersecurity-Skills

# 方式2：Git克隆
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills
```

### 与AI代理集成
将技能库路径配置到平台的技能目录中。以Claude Code为例：
```bash
claude skills add /path/to/Anthropic-Cybersecurity-Skills
```
在对话中可直接调用：
> 使用 analyzing-network-traffic-of-malware 技能分析提供的 pcap 文件。

### 依赖
- Node.js（使用npx时）
- 目标AI平台需支持agentskills.io标准（Claude Code、Copilot等已原生支持）