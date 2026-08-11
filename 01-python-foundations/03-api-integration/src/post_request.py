import requests


url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Generative AI",
    "body": "Learning API integration with Python",
    "userId": 1
}

response = requests.post(
    url,
    json=payload,
    timeout=10
)

print("Status Code:", response.status_code)
print("Response:", response.json())