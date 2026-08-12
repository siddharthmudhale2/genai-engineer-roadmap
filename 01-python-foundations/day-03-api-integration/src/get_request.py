import requests

url = "https://api.github.com"

response = requests.get(url,timeout=10)

print("Status code", response.status_code)
print("Response", response.json())