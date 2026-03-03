import requests

url = "http://127.0.0.1:8000/add"

params = {
    "a": 5,
    "b": 10
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())