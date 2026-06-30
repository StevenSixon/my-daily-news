```bash
pip install supervision  # Python>=3.10
```

**最小可用示例（使用内置 rfdetr 模型）**

```python
import supervision as sv
from PIL import Image
from rfdetr import RFDETRSmall

image = Image.open("path/to/image.jpg")
model = RFDETRSmall()
detections = model.predict(image, threshold=0.5)

print(len(detections))  # e.g., 5

# 可视化
import cv2
image = cv2.imread("path/to/image.jpg")
box_annotator = sv.BoxAnnotator()
annotated = box_annotator.annotate(scene=image.copy(), detections=detections)
cv2.imwrite("annotated.jpg", annotated)
```

更多连接器（如 Ultralytics YOLO）和数据集工具请参阅官方文档。