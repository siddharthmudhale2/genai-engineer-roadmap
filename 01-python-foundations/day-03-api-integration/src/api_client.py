import requests


def get_data(url, params=None, headers=None):
    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")

    return None


def main():
    url = "https://api.github.com"

    data = get_data(url)

    if data:
        print("API Response:")
        print(data)


if __name__ == "__main__":
    main()