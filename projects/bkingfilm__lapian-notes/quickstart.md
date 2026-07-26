## 普通用户（无需编程）
1. 下载最新release的 `lapian-notes-vX.Y.Z.zip`，解压。
2. 双击 `run.bat`（Windows）或 `run.command`（Mac）；首次会自行下载便携Node.js并安装依赖，几分钟后浏览器自动打开工具页面。
3. 按顶部四步向导操作：导入电影 → 将ZIP包发给任意AI分析（支持Kimi等无法传ZIP的AI用散文件方案） → 导回AI返回的JSON → 获得时间轴、结构树、情绪曲线，开始精修笔记。

## 开发者
- 要求：Node.js 20.19+ / 22.12+，Chrome内核浏览器，ffmpeg（可选，用于RMVB/AVI等格式转码）。
- 安装依赖：`npm install`
- 启动开发服务器：`npm run dev`（提供完整本地接口，含转码和字幕搜索）
- 构建静态版本：`npm run build`（会降级转码和字幕搜索为手动操作）
- 测试：`npm run check`（需Node 22.18+）

最小可用示例：导入一部H.264 MP4（无需ffmpeg），让AI分析，导回结果，立即体验完整笔记功能。