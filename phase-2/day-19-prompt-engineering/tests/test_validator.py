import pytest

from src.validator import validate_prompt


def test_valid_prompt():
    prompt = """
    Task:
    Summarize.

    Requirements:
    Be concise.

    <document>
    Python is useful.
    </document>
    """

    validate_prompt(prompt)


def test_invalid_prompt():
    with pytest.raises(ValueError):
        validate_prompt("invalid prompt")