from src.client import FakeLLMClient
from src.models import JobMatch, Recommendation
from src.prompts import RECOMMENDATION_PROMPT


class RecommendationGenerator:
    def __init__(self, client: FakeLLMClient):
        self.client = client

    def generate(
        self,
        match: JobMatch,
    ) -> Recommendation:
        prompt = RECOMMENDATION_PROMPT.format(
            match=match.model_dump_json()
        )

        response = self.client.generate(prompt)

        return Recommendation.model_validate_json(response)