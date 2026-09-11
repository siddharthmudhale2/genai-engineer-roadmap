from src.client import FakeLLMClient
from src.extractor import CandidateExtractor
from src.matcher import JobMatcher
from src.models import Job
from src.recommender import RecommendationGenerator
from src.workflow import JobApplicationWorkflow


def test_full_workflow():
    extraction_response = """
    {
        "name": "John",
        "experience_years": 3,
        "skills": ["Python", "FastAPI"]
    }
    """

    recommendation_response = """
    {
        "decision": "Maybe",
        "reason": "Missing PostgreSQL."
    }
    """

    client = FakeLLMClient(
        [
            extraction_response,
            recommendation_response,
        ]
    )

    workflow = JobApplicationWorkflow(
        extractor=CandidateExtractor(client),
        matcher=JobMatcher(),
        recommender=RecommendationGenerator(client),
    )

    result = workflow.run(
        "John has Python and FastAPI experience.",
        Job(
            title="Backend Developer",
            required_skills=[
                "Python",
                "FastAPI",
                "PostgreSQL",
            ],
            minimum_experience=2,
        ),
    )

    assert result.decision == "Maybe"