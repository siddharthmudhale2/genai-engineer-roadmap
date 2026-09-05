from src.client import FakeLLMClient
from src.service import SummaryService


def main() -> None:
    client = FakeLLMClient()

    service = SummaryService(client)

    document = """
    Python is a high-level programming language.
    It is widely used for web development,
    automation, data science, and artificial intelligence.
    """

    result = service.summarize(document)

    print("Summary:")
    print(result)


if __name__ == "__main__":
    main()