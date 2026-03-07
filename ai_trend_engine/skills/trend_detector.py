from __future__ import annotations

from collections import Counter


class TrendDetector:
    def detect(self, keywords: list[str]) -> Counter[str]:
        return Counter(k.strip() for k in keywords if k.strip())
