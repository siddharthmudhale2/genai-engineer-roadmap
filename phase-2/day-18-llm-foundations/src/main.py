from .model import DemoLLM
from .tokenizer import (
    count_tokens,
    tokenize,
)


def main() -> None:

    prompt = (
        "Explain large language models"
    )

    print("Tokens:")

    print(tokenize(prompt))

    print()

    print("Token count:")

    print(count_tokens(prompt))

    print()

    model = DemoLLM()

    print("Model output:")

    print(
        model.generate(prompt)
    )


if __name__ == "__main__":

    main()