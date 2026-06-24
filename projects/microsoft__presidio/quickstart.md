### 安装
```bash
pip install presidio-analyzer presidio-anonymizer
# 附加图像编辑：pip install presidio-image-redactor
# 附加结构化：pip install presidio-structured
# 下载 spaCy 英文模型（如已安装 presidio-analyzer 可选）
python -m spacy download en_core_web_lg
```

### 最小示例
```python
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

text = "My phone number is 212-555-5555 and email is john@example.com"

# 1. 分析
analyzer = AnalyzerEngine()
results = analyzer.analyze(text=text, entities=[], language='en')

# 2. 匿名化
anonymizer = AnonymizerEngine()
final_text = anonymizer.anonymize(text=text, analyzer_results=results)
print(final_text.text)
# 输出示例：My phone number is <PHONE_NUMBER> and email is <EMAIL_ADDRESS>
```

### 使用 Docker
```bash
docker pull mcr.microsoft.com/presidio-analyzer
docker pull mcr.microsoft.com/presidio-anonymizer
# 启动服务后通过 REST API 调用
```