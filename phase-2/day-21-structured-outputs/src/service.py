from src.client import FakeLLMClient
from src.models import Candidate
from src.parser import parse_candidate
from src.prompts import build_candidate_prompt


class CandidateAnalyzer:
    def __init__(self, client: FakeLLMClient):
        self.client = client

    def analyze(self, candidate_text: str) -> Candidate:
        prompt = build_candidate_prompt(candidate_text)

        response = self.client.generate(prompt)

        return parse_candidate(response)