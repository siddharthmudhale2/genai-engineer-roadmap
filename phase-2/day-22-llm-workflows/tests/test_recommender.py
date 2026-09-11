from src.client import FakeLLMClient
from src.models import JobMatch
from src.recommender import RecommendationGenerator


def test_recommendation():
    response = """
    {
        "decision": "Maybe",
        "reason": "Missing PostgreSQL experience."
    }
    """

    generator = RecommendationGenerator(
        FakeLLMClient([response])
    )

    result = generator.generate(
        JobMatch(
            match_score=66,
            matching_skills=["python", "fastapi"],
            missing_skills=["postgresql"],
        )
    )

    assert result.decision == "Maybe"
    assert "PostgreSQL" in result.reason