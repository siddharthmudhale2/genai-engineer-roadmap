import math


def cosine_similarity(
    a: list[float],
    b: list[float],
) -> float:
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimensions.")

    dot_product = sum(
        x * y
        for x, y in zip(a, b)
    )

    magnitude_a = math.sqrt(
        sum(x * x for x in a)
    )

    magnitude_b = math.sqrt(
        sum(y * y for y in b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError(
            "Cosine similarity is undefined for zero vectors."
        )

    return dot_product / (
        magnitude_a * magnitude_b
    )