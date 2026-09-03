from src.generators import (
    count_numbers,
    square_numbers,
)


def test_count_numbers():

    result = list(
        count_numbers(5)
    )

    assert result == [
        1,
        2,
        3,
        4,
        5
    ]


def test_square_numbers():

    result = list(
        square_numbers(
            range(1, 4)
        )
    )

    assert result == [
        1,
        4,
        9
    ]