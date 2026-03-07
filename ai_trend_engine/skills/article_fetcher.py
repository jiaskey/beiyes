from __future__ import annotations

from newspaper import Article


class ArticleFetcher:
    def fetch(self, url: str) -> str:
        if not url:
            return ""
        try:
            article = Article(url)
            article.download()
            article.parse()
            return article.text
        except Exception:
            return ""
