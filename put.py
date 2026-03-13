import requests
url='http://192.168.1.65:3456/update-user/1'
headers={"accept":"application/json",
         "Content-type":"application/json"}
data={
  "user_id": 1,
  "name": "SATYAJIT",
  "email": "satyajit.rout@c-zentrix.com",
  "address": "gurgaon",
  "phone": "9999999999",
  "occupation": "SDE"
}
response=requests.put(url,headers=headers,json=data)
print(response.status_code)
print(response.json())

