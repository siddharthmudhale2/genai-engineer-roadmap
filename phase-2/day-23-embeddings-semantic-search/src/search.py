from src.embeddings import embed
from src.similarity import cosine_similarity


def search(
    query: str,
    documents: list[str],
    top_k: int = 3,
) -> list[tuple[str, float]]:
    query_vector = embed(query)

    results = []

    for document in documents:
        document_vector = embed(document)
        
        if not any(document_vector):
            continue

        score = cosine_similarity(
            query_vector,
            document_vector,
        )

        results.append((document, score))

    results.sort(
        key=lambda item: item[1],
        reverse=True,
    )

    return results[:top_k]