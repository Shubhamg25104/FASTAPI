import requests
url="http://192.168.1.65:3456/add-users"
data = {
  "user_id": "101",
  "name": "satyajit",
  "email": "satyajit.rout@c-zentrix.com",
  "address": "gurgaon",
  "phone": "9348333098",
  "occupation": "SDE"
}

response=requests.post(url,json=data)
print(response.status_code)
print(response.json())