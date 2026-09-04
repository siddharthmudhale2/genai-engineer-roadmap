def tokenize(text: str) -> list[str]:

    return text.split()


def count_tokens(text: str) -> int:

    return len(tokenize(text))