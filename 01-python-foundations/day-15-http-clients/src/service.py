import httpx


async def fetch_external_data() -> dict:

    async with httpx.AsyncClient(
        timeout=10
    ) as client:

        response = await client.get(
            "https://httpbin.org/get",
            params={
                "source": "fastapi",
                "topic": "genai"
            }
        )

        response.raise_for_status()

        return response.json()