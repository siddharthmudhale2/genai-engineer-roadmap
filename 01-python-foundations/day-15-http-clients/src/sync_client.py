import requests


def fetch_data() -> dict:

    response = requests.get(
        "https://httpbin.org/get",
        params={
            "language": "python",
            "topic": "genai"
        },
        timeout=10
    )

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":

    data = fetch_data()

    print("Status: 200")
    print("URL:", data["url"])