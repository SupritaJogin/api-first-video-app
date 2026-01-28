import requests

TOKEN = "PASTE_YOUR_TOKEN_HERE"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(
    "http://127.0.0.1:5000/auth/profile",
    headers=headers
)

print(response.status_code)
print(response.json())
