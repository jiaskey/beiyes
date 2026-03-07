from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

import yaml

from core.database import DatabaseClient
from skills.article_fetcher import ArticleFetcher
from skills.article_writer import ArticleWriter
from skills.keyword_extract import KeywordExtractor
from skills.rss_reader import RSSReader
from skills.text_cleaner import TextCleaner
from skills.trend_detector import TrendDetector


class TrendPipeline:
    def __init__(self, config_path: str) -> None:
        self.config_path = Path(config_path)
        self.rss_reader = RSSReader()
        self.fetcher = ArticleFetcher()
        self.cleaner = TextCleaner()
        self.extractor = KeywordExtractor()
        self.trend_detector = TrendDetector()
        self.writer = ArticleWriter()
        self.db = DatabaseClient.from_env()

    def _load_sources(self) -> list[str]:
        with self.config_path.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file) or {}
        return config.get("rss_sources", [])

    def run(self) -> dict[str, Any]:
        all_keywords: list[str] = []
        collected_articles: list[dict[str, Any]] = []

        for source in self._load_sources():
            articles = self.rss_reader.read(source)
            for article in articles:
                content = self.fetcher.fetch(article["link"])
                if not content:
                    continue

                cleaned = self.cleaner.clean(content)
                if not cleaned:
                    continue

                keywords = self.extractor.extract(cleaned)
                all_keywords.extend(keywords)

                enriched_article = {
                    **article,
                    "content": cleaned,
                    "keywords": keywords,
                }
                collected_articles.append(enriched_article)
                self.db.insert_article(enriched_article)

        trend_counts = self.trend_detector.detect(all_keywords)
        top_trends = trend_counts.most_common(10)

        generated_articles: list[dict[str, str]] = []
        for topic, _ in top_trends[:3]:
            generated = self.writer.generate(topic)
            payload = {"topic": topic, "content": generated}
            generated_articles.append(payload)
            self.db.insert_generated_article(payload)

        self.db.insert_trends(trend_counts)

        return {
            "article_count": len(collected_articles),
            "keyword_count": len(all_keywords),
            "top_trends": top_trends,
            "generated_articles": generated_articles,
        }
