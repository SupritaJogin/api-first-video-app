import requests

url = "http://127.0.0.1:5000/auth/login"
data = {
    "email": "suprita_new@test.com",  # use the same email you just signed up
    "password": "password123"          # the password you used
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
