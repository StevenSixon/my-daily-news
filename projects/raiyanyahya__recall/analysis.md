## 它是什么
Recall 是 Claude Code 的本地优先插件，自动记录每个会话的活动并生成紧凑摘要（`context.md`），在新会话开始时提供“我们在哪里停下、接下来该做什么”的上下文，无需手动维护 `CLAUDE.md` 或重放冗长历史。

## 为什么火
仓库发布仅 7 天已获 566 Star（截止数据）。隐私与成本是开发者选用 AI 工具的核心顾虑：Recall 完全离线、无 API 调用、不消耗模型 token，却能提供类似 LLM 记忆插件的体验。它直接瞄准了 Claude Code 订阅用户“想持久记忆但不想额外付费或泄露代码”的刚需。

## 技术栈
- 语言：Python（stdlib 优先，numpy 作为可选加速器）
- 摘要算法：自研 TF-IDF + TextRank（基于 PageRank 的抽取式摘要），无任何外部模型依赖
- 集成方式：Claude Code Plugin（hooks + slash commands），SessionStart/Stop/End 钩子驱动
- 输出格式：Markdown（`history.md` 追加日志 + `context.md` 摘要）
- 安全机制：内置秘密信息脱敏、Git 操作硬化、写入路径限制

## 核心能力
- **零配置启动**：安装即用，无需 pip install、API key 或外部服务
- **静默捕获**：会话期间自动增量追加到 `history.md`，失败不影响主会话
- **本地摘要生成**：通过 `/recall:save` 手动触发或设置 `auto_save_context: "on_end"` 自动生成 `context.md`
- **隐私与安全**：无网络调用，读取仅限当前项目会话，可脱敏密钥，Git 命令在沙箱配置下运行
- **灵活使用**：可提交 `.recall/` 作为团队共享记忆，也可 gitignore 保持个人记忆

## 适用场景
- 频繁切换项目或长时间跨度开发，希望 Claude Code 记住历史决策和进展
- 对代码隐私有较高要求，禁止任何第三方 API 访问项目上下文
- 订阅制用户想最大化利用每月 token 配额，避免重复解释消耗
- 团队协作中希望共享会议/开发摘要，但不想引入外部记忆服务

## 同类对比
- **Claude Code 内置 `--continue/--resume`**：重放完整历史，token 成本高且不易迁移；Recall 只注入紧凑摘要（~1-2K tokens），可跨机器使用
- **CLAUDE.md**：手动维护的指令文件，不自动记录实际发生的事；Recall 是自动生成的“发生了什么”记录
- **其他 LLM 记忆工具（如 Mem0, LangMem）**：依赖外部模型调用，有隐私和成本顾虑；Recall 完全本地并无额外开销
- **差异化优势**：唯一的全本地、零模型调用、零网络访问的 Claude Code 记忆方案

## 版本动态
- v0.3.6（2026-06-25）修复了 Windows 下的三个关键问题：`python3` 找不到、转录目录路径编码错误、控制台因 emoji 崩溃，使 Windows 用户首次可正常使用。
- 最新特性：支持自动保存（`on_end`）、可暂停捕获、纯 Python fallback 保证环境兼容性。
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**