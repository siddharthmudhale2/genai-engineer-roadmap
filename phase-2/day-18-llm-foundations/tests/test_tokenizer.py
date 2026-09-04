from src.tokenizer import (
    count_tokens,
    tokenize,
)


def test_tokenize():

    result = tokenize(
        "Python is powerful"
    )

    assert result == [
        "Python",
        "is",
        "powerful"
    ]


def test_count_tokens():

    assert count_tokens(
        "Python is powerful"
    ) == 3