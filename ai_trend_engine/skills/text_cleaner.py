from __future__ import annotations

import re


class TextCleaner:
    def clean(self, text: str) -> str:
        if not text:
            return ""
        cleaned = re.sub(r"<[^>]+>", " ", text)
        cleaned = re.sub(r"\s+", " ", cleaned)
        return cleaned.strip()
