import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
app_env = os.getenv("APP_ENV")

if not api_key:
    raise ValueError("Api key is not configured")

print("Api key loaded successfully")
print("Application environment", app_env)
