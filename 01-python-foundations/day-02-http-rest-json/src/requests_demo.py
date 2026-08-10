import requests

def main():
    url = "https://api.github.com"
    
    response = requests.get(url)
    
    print("Status code :",response.status_code)
    print("Content Type : ", response.headers.get("Content-Type"))
    
    print("Response ", response.text[:500])
    
if __name__ == "__main__":
    main()