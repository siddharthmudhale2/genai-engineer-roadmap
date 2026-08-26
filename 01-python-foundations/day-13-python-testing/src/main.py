from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="Day 13 Testing API",
    version="1.0.0"
)


class User(BaseModel):

    name: str = Field(
        min_length=2
    )

    age: int = Field(
        ge=18,
        le=100
    )


@app.get("/")
def home():

    return {
        "message": "Testing API"
    }


@app.post("/users")
def create_user(
    user: User
):

    return {
        "message": "User created",
        "user": user
    }