import asyncio

import httpx


async def fetch_data() -> dict:

    async with httpx.AsyncClient(
        timeout=10
    ) as client:

        response = await client.get(
            "https://httpbin.org/get",
            params={
                "language": "python",
                "topic": "genai"
            }
        )

        response.raise_for_status()

        return response.json()


async def main() -> None:

    data = await fetch_data()

    print("Status: 200")
    print("URL:", data["url"])


if __name__ == "__main__":

    asyncio.run(main())