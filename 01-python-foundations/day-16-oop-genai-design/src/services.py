from .providers import LLMProvider


class ChatService:

    def __init__(
        self,
        provider: LLMProvider
    ) -> None:

        self.provider = provider

    def chat(
        self,
        message: str
    ) -> str:

        cleaned_message = (
            message.strip()
        )

        if not cleaned_message:
            raise ValueError(
                "Message cannot be empty."
            )

        return self.provider.generate(
            cleaned_message
        )