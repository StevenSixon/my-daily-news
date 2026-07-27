**安装/运行**
```bash
# 仅需Docker，用模拟数据立即体验
docker pull ruvnet/wifi-densepose:latest
docker run -p 3000:3000 ruvnet/wifi-densepose:latest
# 打开 http://localhost:3000
```

**ESP32硬件实采**
1. 刷写固件：
```bash
python -m esptool --chip esp32s3 --port COM9 --baud 460800 \
  write_flash 0x0 bootloader.bin 0x8000 partition-table.bin \
  0xf000 ota_data_initial.bin 0x20000 esp32-csi-node.bin
```
2. 配网并指向目标IP

**依赖前提**
- Docker或Rust 1.85+环境
- 硬件实采需ESP32-S3（或C6），WiFi AP可工作
- 可选：Cognitum Seed用于长期存储和向量检索