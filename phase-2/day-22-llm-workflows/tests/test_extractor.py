from src.client import FakeLLMClient
from src.extractor import CandidateExtractor


def test_candidate_extraction():
    response = """
    {
        "name": "John",
        "experience_years": 3,
        "skills": ["Python", "FastAPI"]
    }
    """

    extractor = CandidateExtractor(
        FakeLLMClient([response])
    )

    candidate = extractor.extract(
        "John has three years of Python experience."
    )

    assert candidate.name == "John"
    assert candidate.experience_years == 3
    assert "Python" in candidate.skills