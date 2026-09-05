from src.client import LLMClient
from src.prompts import build_summary_prompt


class SummaryService:
    def __init__(self, client: LLMClient):
        self.client = client

    def summarize(self, document: str) -> str:
        prompt = build_summary_prompt(document)

        return self.client.generate(prompt)