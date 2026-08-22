import logging


logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    ),
    filename="logs/app.log"
)

logger = logging.getLogger(__name__)


def divide_numbers(
    a: float,
    b: float
) -> float:

    if b == 0:
        raise ValueError(
            "The denominator cannot be zero."
        )

    return a / b


def main() -> None:

    logger.info(
        "Application started"
    )

    try:

        result = divide_numbers(
            100,
            0
        )

        logger.info(
            "Calculation result: %s",
            result
        )

    except ValueError:

        logger.exception(
            "Calculation failed"
        )

    finally:

        logger.info(
            "Application finished"
        )


if __name__ == "__main__":
    main()