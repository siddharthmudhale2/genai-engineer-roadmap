from src.client import FakeLLMClient
from src.service import SummaryService


def test_summary_service():
    client = FakeLLMClient()
    service = SummaryService(client)

    result = service.summarize(
        "Python is a programming language."
    )

    assert result == "This is a simulated LLM response."