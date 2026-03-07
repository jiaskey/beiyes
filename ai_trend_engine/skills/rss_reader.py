from __future__ import annotations

from typing import Any

import feedparser


class RSSReader:
    def read(self, feed_url: str) -> list[dict[str, Any]]:
        feed = feedparser.parse(feed_url)
        items: list[dict[str, Any]] = []

        for entry in feed.entries:
            items.append(
                {
                    "title": entry.get("title", ""),
                    "link": entry.get("link", ""),
                    "published": entry.get("published", ""),
                }
            )
        return items
