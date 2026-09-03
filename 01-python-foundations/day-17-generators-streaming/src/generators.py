def count_numbers(
    limit: int
):

    for number in range(1, limit + 1):

        yield number


def square_numbers(
    numbers
):

    for number in numbers:

        yield number * number


def read_lines(
    filename: str
):

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            yield line.rstrip()