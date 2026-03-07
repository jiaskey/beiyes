from __future__ import annotations

import os

from openai import OpenAI


class ArticleWriter:
    def __init__(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else None

    def generate(self, trend_topic: str) -> str:
        if not trend_topic:
            return ""

        prompt = (
            f"趋势主题：{trend_topic}\n"
            "请输出一篇趋势分析文章，结构必须包含：\n"
            "1. 趋势解释\n"
            "2. 技术背景\n"
            "3. 行业影响\n"
            "4. 未来发展\n"
        )

        if self.client is None:
            return f"[Demo] {trend_topic} 趋势分析：请配置 OPENAI_API_KEY 后启用真实生成。"

        response = self.client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            input=prompt,
        )
        return response.output_text
