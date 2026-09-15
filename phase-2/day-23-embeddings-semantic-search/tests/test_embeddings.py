from src.embeddings import embed, tokenize


def test_tokenize():
    result = tokenize(
        "Python is great!"
    )

    assert result == [
        "python",
        "is",
        "great",
    ]


def test_embedding_dimension():
    vector = embed("Python programming")

    assert len(vector) == 10


def test_python_embedding():
    vector = embed("Python")

    assert vector[0] == 1.0