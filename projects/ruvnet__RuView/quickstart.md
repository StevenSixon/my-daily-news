## 安装与最小可用示例

### 前置依赖
- 无硬件？直接 Docker 体验（无需 ESP32 或传感器）。
- 真实环境：1 个以上 ESP32-S3 开发板（≥ $9）、WiFi 路由器、Python 3.10+。

### Docker 快速启动
```bash
docker pull ruvnet/wifi-densepose:latest
docker run -p 3000:3000 ruvnet/wifi-densepose:latest
# 打开 http://localhost:3000，使用模拟数据观察感知效果。
```

### 用 ESP32-S3 硬件搭建真实感知节点
```bash
# 1. 烧录固件
python -m esptool --chip esp32s3 --port /dev/ttyUSB0 --baud 460800 \
  write_flash 0x0 bootloader.bin 0x8000 partition-table.bin \
  0xf000 ota_data_initial.bin 0x20000 esp32-csi-node.bin

# 2. 配置 WiFi 并指向上位机
python firmware/esp32-csi-node/provision.py --port /dev/ttyUSB0 \
  --ssid "YourWiFi" --password "secret" --target-ip 192.168.1.20
```
传感器自动开始采集 CSI，上位机运行的 RuView 服务即可实时可视化并反馈生命体征、姿态等信息。

### Python 包（PyO3）
```bash
pip install ruview
# 导入模型，离线推理
from ruview import WifiDensepose
model = WifiDensepose.from_pretrained("ruvnet/wifi-densepose-pretrained")
embedding = model.encode(your_csi_tensor)
```
更多详见 [`docs/user-guide.md`] 与 [官方主页](https://Cognitum.One/RuView)。