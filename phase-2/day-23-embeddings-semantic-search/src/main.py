from src.embeddings import embed
from src.search import search


DOCUMENTS = [
    "Python is a programming language.",
    "FastAPI is a Python web framework.",
    "PostgreSQL is a relational database.",
    "Machine learning uses algorithms to learn from data.",
]


def main() -> None:
    print("Example Vector:")
    print(embed("Python programming"))

    print("\nSemantic Search Results:")

    query = "Python programming"

    results = search(
        query=query,
        documents=DOCUMENTS,
        top_k=3,
    )

    for document, score in results:
        print(f"{score:.4f} → {document}")


if __name__ == "__main__":
    main()