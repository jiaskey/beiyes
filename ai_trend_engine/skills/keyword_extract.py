from __future__ import annotations

from functools import cached_property

from keybert import KeyBERT


class KeywordExtractor:
    @cached_property
    def model(self) -> KeyBERT:
        return KeyBERT()

    def extract(self, text: str, top_k: int = 5) -> list[str]:
        if not text:
            return []
        keywords = self.model.extract_keywords(
            text,
            top_n=top_k,
            stop_words="english",
            keyphrase_ngram_range=(1, 2),
        )
        return [keyword for keyword, _ in keywords]
