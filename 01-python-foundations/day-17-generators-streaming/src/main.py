from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from .streaming import stream_words


app = FastAPI(
    title="GenAI Streaming Demo",
    version="1.0.0"
)


@app.get("/")
def home() -> dict[str, str]:

    return {
        "message": "Streaming API"
    }


@app.get("/stream")
async def stream():

    return StreamingResponse(
        stream_words(
            "Python generators enable streaming"
        ),
        media_type="text/plain"
    )