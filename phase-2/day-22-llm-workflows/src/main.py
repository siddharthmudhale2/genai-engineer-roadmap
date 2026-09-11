from src.client import FakeLLMClient
from src.extractor import CandidateExtractor
from src.matcher import JobMatcher
from src.models import Job
from src.recommender import RecommendationGenerator
from src.workflow import JobApplicationWorkflow


def main() -> None:
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
        "reason": "The candidate has strong Python and FastAPI experience but is missing PostgreSQL."
    }
    """

    client = FakeLLMClient(
        [
            extraction_response,
            recommendation_response,
        ]
    )

    extractor = CandidateExtractor(client)
    matcher = JobMatcher()
    recommender = RecommendationGenerator(client)

    workflow = JobApplicationWorkflow(
        extractor=extractor,
        matcher=matcher,
        recommender=recommender,
    )

    job = Job(
        title="Backend Developer",
        required_skills=[
            "Python",
            "FastAPI",
            "PostgreSQL",
        ],
        minimum_experience=2,
    )

    result = workflow.run(
        candidate_text=(
            "John has 3 years of Python experience "
            "and has worked with FastAPI."
        ),
        job=job,
    )

    print("Final Recommendation:")
    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()