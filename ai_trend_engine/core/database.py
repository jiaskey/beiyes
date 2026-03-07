from __future__ import annotations

import os
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

import psycopg2
from psycopg2.extras import Json


@dataclass
class DatabaseClient:
    dsn: str

    @classmethod
    def from_env(cls) -> "DatabaseClient":
        dsn = os.getenv("DATABASE_URL", "")
        return cls(dsn=dsn)

    def _connect(self):
        if not self.dsn:
            return None
        return psycopg2.connect(self.dsn)

    def insert_article(self, article: dict[str, Any]) -> None:
        connection = self._connect()
        if connection is None:
            return
        with connection, connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO articles (title, url, content, created_at, keywords)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    article.get("title"),
                    article.get("link"),
                    article.get("content"),
                    datetime.now(timezone.utc),
                    Json(article.get("keywords", [])),
                ),
            )

    def insert_trends(self, trends: Counter[str]) -> None:
        connection = self._connect()
        if connection is None:
            return
        with connection, connection.cursor() as cursor:
            for keyword, count in trends.items():
                cursor.execute(
                    """
                    INSERT INTO trends (keyword, count, date)
                    VALUES (%s, %s, %s)
                    """,
                    (keyword, count, datetime.now(timezone.utc).date()),
                )

    def insert_generated_article(self, article: dict[str, str]) -> None:
        connection = self._connect()
        if connection is None:
            return
        with connection, connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO generated_articles (topic, content, created_at)
                VALUES (%s, %s, %s)
                """,
                (
                    article.get("topic"),
                    article.get("content"),
                    datetime.now(timezone.utc),
                ),
            )
