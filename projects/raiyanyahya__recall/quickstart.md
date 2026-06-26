## 安装
### 从 Marketplace 安装（推荐）
```bash
/plugin marketplace add raiyanyahya/recall
/plugin install recall@recall
```
### 本地开发模式
```bash
git clone https://github.com/raiyanyahya/recall
claude --plugin-dir ./recall
```
无需 pip install，插件自带依赖。

## 最小可用示例
1. 启动 Claude Code 会话，开始任何开发工作（插件自动捕获到 `.recall/history.md`）。
2. 结束前运行 `/recall:save` 生成摘要，或配置自动保存（见“配置”）。
3. 新会话启动时，Recall 会询问是否从 `context.md` 恢复记忆，选择是即可继承上次上下文。

## 配置（可选）
在项目根目录创建 `recall.config.json`：
```json
{
  "auto_save_context": "on_end",
  "summary_sentences": 8,
  "redact": true,
  "include_git": true
}
```

## 依赖前提
- 已安装并登录 Claude Code（`claude` CLI）
- Python 3.9+（系统自带或虚拟环境，安装时不需额外操作）
- numpy 可选（提升大型会话摘要速度）