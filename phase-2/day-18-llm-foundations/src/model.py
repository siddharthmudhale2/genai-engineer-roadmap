from .tokenizer import tokenize


class DemoLLM:

    def __init__(
        self,
        model_name: str = "demo-llm"
    ) -> None:

        self.model_name = model_name

    def generate(
        self,
        prompt: str
    ) -> str:

        tokens = tokenize(prompt)

        token_count = len(tokens)

        return (
            f"[{self.model_name}] "
            f"Received {token_count} tokens. "
            f"Prompt: {prompt}"
        )