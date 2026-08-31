from abc import ABC, abstractmethod


class LLMProvider(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str
    ) -> str:
        """Generate a response."""
        raise NotImplementedError


class CloudLLMProvider(LLMProvider):

    def __init__(
        self,
        model: str
    ) -> None:

        self.model = model

    def generate(
        self,
        prompt: str
    ) -> str:

        return (
            f"[Cloud:{self.model}] "
            f"Response to: {prompt}"
        )


class LocalLLMProvider(LLMProvider):

    def __init__(
        self,
        model: str
    ) -> None:

        self.model = model

    def generate(
        self,
        prompt: str
    ) -> str:

        return (
            f"[Local:{self.model}] "
            f"Response to: {prompt}"
        )