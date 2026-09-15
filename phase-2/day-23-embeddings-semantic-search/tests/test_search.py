from src.search import search


DOCUMENTS = [
    "Python is a programming language.",
    "PostgreSQL is a relational database.",
    "Dogs are household pets.",
]


def test_search_returns_results():
    results = search(
        query="Python programming",
        documents=DOCUMENTS,
        top_k=2,
    )

    assert len(results) == 2


def test_python_document_is_top_result():
    results = search(
        query="Python programming",
        documents=DOCUMENTS,
        top_k=3,
    )

    assert results[0][0] == (
        "Python is a programming language."
    )