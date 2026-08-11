import requests


url = "https://api.github.com"

headers = {
    "Accept": "application/json",
    "User-Agent": "GenAI-Learning-Project"
}

response = requests.get(
    url,
    headers=headers,
    timeout=10
)

print("Status Code:", response.status_code)
print(response.json())