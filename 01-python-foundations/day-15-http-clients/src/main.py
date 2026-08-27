from fastapi import FastAPI

from .service import fetch_external_data


app = FastAPI(
    title="HTTP Client Integration API",
    version="1.0.0"
)


@app.get("/")
def home() -> dict[str, str]:

    return {
        "message": "HTTP Client API"
    }


@app.get("/external")
async def external():

    data = await fetch_external_data()

    return {
        "url": data["url"],
        "args": data["args"]
    }