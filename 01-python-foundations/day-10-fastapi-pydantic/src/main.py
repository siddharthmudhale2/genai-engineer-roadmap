from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(
    title="GenAI Engineer Learning API",
    description="Day 10 FastAPI + Pydantic Practice",
    version="1.0.0"
)


class UserCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50
    )

    age: int = Field(
        ge=18,
        le=100
    )


class UserResponse(BaseModel):
    id: int
    name: str
    age: int


class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=1000
    )

    temperature: float = Field(
        ge=0.0,
        le=2.0,
        default=0.7
    )


class ChatResponse(BaseModel):
    answer: str


@app.get("/")
def home() -> dict[str, str]:
    return {
        "message": "FastAPI + Pydantic API is running"
    }


@app.get(
    "/users/{user_id}",
    response_model=UserResponse
)
def get_user(user_id: int) -> UserResponse:

    if user_id != 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return UserResponse(
        id=1,
        name="Siddharth",
        age=25
    )


@app.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserCreate) -> UserResponse:

    return UserResponse(
        id=1,
        name=user.name,
        age=user.age
    )


@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest) -> ChatResponse:

    answer = (
        f"Received your message: {request.message}"
    )

    return ChatResponse(
        answer=answer
    )