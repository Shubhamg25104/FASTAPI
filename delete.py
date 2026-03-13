import requests
url='http://192.168.1.65:3456/delete-user/101'
headers={"accept":"application/json"}
response=requests.delete(url,headers=headers)
print(response.status_code)
print(response.json()) 