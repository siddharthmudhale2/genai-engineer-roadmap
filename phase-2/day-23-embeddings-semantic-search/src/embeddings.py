import re


VOCABULARY = [
    "python",
    "programming",
    "fastapi",
    "database",
    "postgresql",
    "machine",
    "learning",
    "web",
    "api",
    "coding",
]


def tokenize(text: str) -> list[str]:
    return re.findall(
        r"\b[a-zA-Z]+\b",
        text.lower(),
    )


def embed(text: str) -> list[float]:
    tokens = tokenize(text)

    return [
        float(tokens.count(word))
        for word in VOCABULARY
    ]