## 安装
1. 下载 macOS 应用：Apple Silicon 或 Intel 版本
2. 或通过 npx 安装技能：`npx skills add citrolabs/ego-lite`
3. 首次启动选择是否迁移 Chrome 数据（推荐），获得已有登录态

## 最小可用示例
在代理 CLI 中输入：
```
ego-browser follow @ego_agent on x.com for me
```
代理会调用 skill，在独立空间打开网页、读取快照并操作，你的标签页不受影响。