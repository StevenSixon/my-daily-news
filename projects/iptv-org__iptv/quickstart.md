**前提**：一个支持m3u直播流的视频播放器，如[VLC media player](https://www.videolan.org/)、Kodi、IPTV Smarters、OBS等。

### 最小可用示例
1. 打开VLC（或其他播放器）。
2. 按下 `Ctrl + N`（打开网络流）。
3. 粘贴以下URL并确定：
   ```
   https://iptv-org.github.io/iptv/index.m3u
   ```
4. 播放器加载频道列表后，双击任一频道即可播放。

### 进阶用法
- **分类列表**：查阅 [PLAYLISTS.md](PLAYLISTS.md) 获取按国家/语言分组的m3u链接。
- **本地使用**：`git clone https://github.com/iptv-org/iptv.git` 后，用播放器直接打开本地m3u文件。
- **API调用**：GET请求 `https://iptv-org.github.io/iptv/` 相关端点（实际API文档在`iptv-org/api`仓库）。
- **集成EPG**：下载 `iptv-org/epg` 生成的XMLTV文件，导入播放器获得节目单。

### 注意
频道链接来自第三方，有效性随时变化。如遇死链，可等待仓库自动更新或手动提交issue。