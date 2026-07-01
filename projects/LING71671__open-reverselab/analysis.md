## 它是什么
一个开源逆向工程实验室，将结构化的攻击知识库（197篇文章）与MCP工具链深度结合，使AI Agent能够根据目标信号（URL、APK、PE等）自动选择攻击板，查找知识库中的攻击链并调用对应工具执行。项目完全围绕Agent原生设计，目录结构即工作流约定。

## 为什么火
- 首次将MCP协议大规模应用于逆向工程自动化，打通了“信号→知识→工具”的Agent闭环。
- 197篇按Scenario→Method→Attack chain→MCP mapping结构编写的知识库，直接可被Agent消费。
- README中故意保留“让几乎所有AI都会越狱的bug”，引发安全社区和AI研究者猎奇探索。
- 新建3周即获281星，话题性与实用性兼具。

## 技术栈
- 语言：Python（工具脚本）+ PowerShell（安装/环境引导）
- 核心协议：Model Context Protocol (MCP)
- 分析工具：Ghidra (headless)、Frida、x64dbg、JADX、rizin等
- 环境管理：Bootstrap脚本、模块化安装（CTF/Android/Windows/Common）
- Agent上下文链：CLAUDE.md → AGENTS.md → AI-USAGE.md → boards/<board>/AI-USAGE.md

## 核心能力
1. **信号路由**：根据输入类型（HTTP/APK/PE/加密协议等）自动映射到专用攻击板。
2. **知识库驱动**：每篇文章均定义攻击链与对应的MCP工具映射，Agent无需自行推理工具调用。
3. **目录即工作流**：`samples/`、`exports/`、`reports/`等约定，规范分析产出物。
4. **多平台覆盖**：Web安全（CTF）、Android逆向、Windows PE分析、通用密码/协议破解。
5. **一键健康检查**：提供`lab_healthcheck.py`和`ai_toolcheck.py`验证环境完整性。

## 适用场景
- CTF选手快速自动化解题，利用信号驱动节省信息搜集时间。
- 恶意软件分析师批量处理样本，通过知识库模板输出标准化报告。
- 安全研究者定制攻击链，扩展自己的知识库和MCP工具。
- AI Agent开发者研究越狱漏洞与Agent安全性。

## 同类对比
- vs 单一逆向脚本集（如GhidraScripts）：本项目提供编排层，由Agent决策而非预设线性流程。
- vs 漏洞扫描器（如AutoRecon）：聚焦逆向而非服务扫描，知识库结构针对二进制/Web手工攻击链。
- vs 其他MCP工具集：首次将逆向知识库标准化为Agent可检索的格式，并实现“板”级上下文切换。

## 版本动态
- 创建于2026-06-17，最近推送2026-07-01，处于活跃迭代初期。
- 当前重点：完善知识库覆盖、安装脚本兼容性、Agent上下文链。
- 已知含通用AI越狱缺陷，作者标记为特性暂不修复。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：知识库具体内容质量与示例未展示；AI Agent 集成方式未明确说明（仅暗示通过上下文文件驱动）；越狱bug的具体技术细节和影响面未解释；MCP 工具的实现语言与协议细节未披露；无基准测试数据或成功率统计