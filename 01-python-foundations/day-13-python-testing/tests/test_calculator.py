import pytest

from src.calculator import (
    add,
    divide,
    multiply,
    subtract,
)


def test_add():

    assert add(2, 3) == 5


def test_subtract():

    assert subtract(10, 4) == 6


def test_multiply():

    assert multiply(3, 4) == 12


def test_divide():

    assert divide(10, 2) == 5


def test_divide_by_zero():

    with pytest.raises(
        ValueError,
        match="Cannot divide by zero"
    ):
        divide(10, 0)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (10, 20, 30),
        (-5, 5, 0),
    ]
)
def test_add_multiple_values(
    a,
    b,
    expected
):

    assert add(a, b) == expected