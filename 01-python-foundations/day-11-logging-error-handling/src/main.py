import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    )
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Day 11 Logging API",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home() -> dict[str, str]:

    logger.info(
        "Home endpoint called"
    )

    return {
        "message": "Logging API is running"
    }


@app.post("/chat")
def chat(
    request: ChatRequest
) -> dict[str, str]:

    logger.info(
        "Chat request received"
    )

    if not request.message.strip():

        logger.warning(
            "Empty chat message received"
        )

        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty"
        )

    logger.info(
        "Processing chat request"
    )

    return {
        "answer": (
            f"Received: {request.message}"
        )
    }