# AI Trend Engine

AI趋势挖掘与内容生成系统，流程为：

RSS抓取 → 正文抓取 → 文本清洗 → 关键词提取 → 趋势检测 → AI文章生成 → 数据库存储。

## 快速开始

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 配置环境变量：
   - `DATABASE_URL`：PostgreSQL连接串（可选）
   - `OPENAI_API_KEY`：OpenAI密钥（可选）
3. 运行：
   ```bash
   python main.py
   ```

## 目录

```text
ai_trend_engine/
├── main.py
├── config/
│   └── sources.yaml
├── core/
│   ├── database.py
│   └── pipeline.py
└── skills/
    ├── article_fetcher.py
    ├── article_writer.py
    ├── keyword_extract.py
    ├── rss_reader.py
    ├── text_cleaner.py
    └── trend_detector.py
```
