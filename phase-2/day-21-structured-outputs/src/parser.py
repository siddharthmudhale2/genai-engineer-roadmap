from pydantic import ValidationError

from src.models import Candidate


def parse_candidate(response: str) -> Candidate:
    try:
        return Candidate.model_validate_json(response)
    except ValidationError as exc:
        raise ValueError(
            f"Invalid candidate response: {exc}"
        ) from exc