from fastapi import FastAPI

from .config import settings
from .models import Message
from .services import process_message


app = FastAPI(
    title=settings.app_name,
    version="1.0.0"
)


@app.get("/")
def home() -> dict[str, str]:

    return {
        "message": settings.app_name,
        "environment": settings.environment
    }


@app.post("/process")
def process(
    request: Message
) -> dict[str, str]:

    result = process_message(
        request.message
    )

    return {
        "result": result
    }