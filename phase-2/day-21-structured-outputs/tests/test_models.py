import pytest
from pydantic import ValidationError

from src.models import Candidate


def test_valid_candidate():
    candidate = Candidate(
        name="John",
        experience_years=3,
        skills=["Python", "FastAPI"],
        suitable=True,
    )

    assert candidate.name == "John"
    assert candidate.experience_years == 3
    assert candidate.skills == ["Python", "FastAPI"]
    assert candidate.suitable is True


def test_negative_experience():
    with pytest.raises(ValidationError):
        Candidate(
            name="John",
            experience_years=-1,
            skills=["Python"],
            suitable=True,
        )


def test_empty_name():
    with pytest.raises(ValidationError):
        Candidate(
            name="",
            experience_years=2,
            skills=["Python"],
            suitable=True,
        )