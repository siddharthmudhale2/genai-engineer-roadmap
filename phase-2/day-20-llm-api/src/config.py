import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    api_key: str
    model: str


def get_settings() -> Settings:
    api_key = os.getenv("LLM_API_KEY")
    model = os.getenv("LLM_MODEL")

    if not api_key:
        raise RuntimeError("LLM_API_KEY is not configured.")

    if not model:
        raise RuntimeError("LLM_MODEL is not configured.")

    return Settings(
        api_key=api_key,
        model=model,
    )