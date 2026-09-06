from pydantic import BaseModel, Field


class Candidate(BaseModel):
    name: str = Field(min_length=1)
    experience_years: int = Field(ge=0)
    skills: list[str]
    suitable: bool