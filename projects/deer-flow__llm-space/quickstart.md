## 安装
1. 从 [GitHub Releases](https://github.com/deer-flow/llm-space/releases/latest) 下载 macOS DMG（Apple Silicon 或 Intel），可选标准版或高性能版。
2. 安装后启动，线程与设置自动保存于 `~/.llm-space`。

## 从源码运行
- 需要 Bun 环境（推荐用 mise 锁定版本），在仓库根目录执行 `bun install`。
- 启动桌面开发模式：`mise run dev`. 
- 构建金丝雀版本：`mise run build:canary`.

## 最小可用示例
1. 打开应用后创建新线程，选择模型提供商（如火山引擎 Coding Plan 或 OpenAI）。
2. 编写系统提示与工具定义（或使用 AI 生成）。
3. 发送用户消息，观察追踪面板中每一步的模型输入输出、工具调用结果。
4. 运行结束后可在历史面板回放，检查每步细节。