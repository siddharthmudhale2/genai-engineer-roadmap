import pytest

from src.config import get_settings


def test_missing_api_key(monkeypatch):
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    monkeypatch.setenv("LLM_MODEL", "test-model")

    with pytest.raises(RuntimeError):
        get_settings()