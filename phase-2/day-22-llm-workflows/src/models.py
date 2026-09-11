from pydantic import BaseModel, Field


class Candidate(BaseModel):
    name: str
    experience_years: int = Field(ge=0)
    skills: list[str]


class Job(BaseModel):
    title: str
    required_skills: list[str]
    minimum_experience: int = Field(ge=0)


class JobMatch(BaseModel):
    match_score: int = Field(ge=0, le=100)
    matching_skills: list[str]
    missing_skills: list[str]


class Recommendation(BaseModel):
    decision: str
    reason: str