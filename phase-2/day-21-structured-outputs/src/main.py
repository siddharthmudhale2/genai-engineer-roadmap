from src.client import FakeLLMClient
from src.service import CandidateAnalyzer


def main() -> None:
    response = """
    {
        "name": "John",
        "experience_years": 3,
        "skills": ["Python", "FastAPI"],
        "suitable": true
    }
    """

    client = FakeLLMClient(response)

    analyzer = CandidateAnalyzer(client)

    candidate_text = """
    John has 3 years of Python experience.
    He has worked with FastAPI and backend systems.
    """

    candidate = analyzer.analyze(candidate_text)

    print("Candidate:")
    print(candidate)
    print()
    print("Name:", candidate.name)
    print("Experience:", candidate.experience_years)
    print("Skills:", candidate.skills)
    print("Suitable:", candidate.suitable)


if __name__ == "__main__":
    main()