from src.matcher import JobMatcher
from src.models import Candidate, Job


def test_job_matcher():
    candidate = Candidate(
        name="John",
        experience_years=3,
        skills=["Python", "FastAPI"],
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

    result = JobMatcher().match(
        candidate,
        job,
    )

    assert result.match_score == 66
    assert "python" in result.matching_skills
    assert "postgresql" in result.missing_skills