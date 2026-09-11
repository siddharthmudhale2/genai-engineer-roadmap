from src.client import FakeLLMClient
from src.models import Candidate
from src.prompts import EXTRACTION_PROMPT


class CandidateExtractor:
    def __init__(self, client: FakeLLMClient):
        self.client = client

    def extract(self, candidate_text: str) -> Candidate:
        if not candidate_text.strip():
            raise ValueError("Candidate text cannot be empty.")

        prompt = EXTRACTION_PROMPT.format(
            candidate_text=candidate_text
        )

        response = self.client.generate(prompt)

        return Candidate.model_validate_json(response)