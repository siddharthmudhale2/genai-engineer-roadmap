import pytest

from src.parser import parse_candidate


def test_parse_valid_candidate():
    response = """
    {
        "name": "John",
        "experience_years": 3,
        "skills": ["Python", "FastAPI"],
        "suitable": true
    }
    """

    candidate = parse_candidate(response)

    assert candidate.name == "John"
    assert candidate.experience_years == 3
    assert "Python" in candidate.skills
    assert candidate.suitable is True