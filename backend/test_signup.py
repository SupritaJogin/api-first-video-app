import requests

url = "http://127.0.0.1:5000/auth/signup"
data = {
    "name": "Suprita",
    "email": "suprita3@test.com",   # change number
    "password": "password123"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
