import pytest

from src.providers import LLMProvider
from src.services import ChatService


class FakeLLMProvider(LLMProvider):

    def generate(
        self,
        prompt: str
    ) -> str:

        return (
            f"Fake response: {prompt}"
        )


def test_chat_service() -> None:

    provider = FakeLLMProvider()

    service = ChatService(
        provider=provider
    )

    result = service.chat(
        "Explain RAG"
    )

    assert result == (
        "Fake response: Explain RAG"
    )


def test_chat_service_strips_input() -> None:

    provider = FakeLLMProvider()

    service = ChatService(
        provider=provider
    )

    result = service.chat(
        "   Explain RAG   "
    )

    assert result == (
        "Fake response: Explain RAG"
    )


def test_empty_message() -> None:

    provider = FakeLLMProvider()

    service = ChatService(
        provider=provider
    )

    with pytest.raises(
        ValueError,
        match="Message cannot be empty"
    ):
        service.chat("   ")