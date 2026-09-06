import pytest

from src.client import FakeLLMClient
from src.service import CandidateAnalyzer


def test_candidate_analysis():
    response = """
    {
        "name": "John",
        "experience_years": 3,
        "skills": ["Python", "FastAPI"],
        "suitable": true
    }
    """

    analyzer = CandidateAnalyzer(
        FakeLLMClient(response)
    )

    result = analyzer.analyze(
        "John has three years of Python experience."
    )

    assert result.name == "John"
    assert result.experience_years == 3
    assert result.suitable is True


def test_invalid_llm_response():
    response = """
    {
        "name": "John",
        "experience_years": -2,
        "skills": ["Python"],
        "suitable": true
    }
    """

    analyzer = CandidateAnalyzer(
        FakeLLMClient(response)
    )

    with pytest.raises(ValueError):
        analyzer.analyze("John has Python experience.")