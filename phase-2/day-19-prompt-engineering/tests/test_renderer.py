import pytest

from src.renderer import render_summary_prompt


def test_render_summary_prompt():
    document = "Python is a programming language."

    prompt = render_summary_prompt(document)

    assert "Python is a programming language." in prompt
    assert "<document>" in prompt
    assert "</document>" in prompt


def test_empty_document():
    with pytest.raises(ValueError):
        render_summary_prompt("")