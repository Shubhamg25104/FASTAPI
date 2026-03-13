import requests

url = 'http://192.168.1.65:3456/get-user/1'

headers = {
    "accept": "application/json"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())