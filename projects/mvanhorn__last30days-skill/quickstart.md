## 安装
### Claude Code（推荐，自动更新）
```bash
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```
### 其他Agent Skills主机（Codex, Cursor, Copilot等）
要求：Node.js 环境
```bash
npx skills add mvanhorn/last30days-skill -g
```
（`-g` 全局安装，可跨项目使用；省略则项目级安装）

## 最小可用示例
```bash
/last30days Peter Steinberger
```
自动搜索Reddit、X、HN、Polymarket、GitHub（零配置），返回含社会信号评分的合成简报。

## 扩展数据源
首次运行时自动弹出设置向导，引导配置X、YouTube、TikTok、Instagram等需要API密钥或浏览器会话的平台，30秒内完成。Reddit、HN、Polymarket、GitHub无需任何配置立即可用。

## 生成HTML简报
```bash
/last30days OpenClaw --emit=html
```
或在对话中自然语言要求“给我一份可分享的HTML简报”。文件保存至 `~/Documents/Last30Days/`。

## 依赖前提
- Claude Code（或兼容Agent Skills的AI编程工具）
- Node.js（用于npx安装）
- 基本源无需额外依赖；高级源需自行获取对应平台API密钥/会话