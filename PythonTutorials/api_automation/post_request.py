'''
Created on 30-Nov-2025

@author: Vivek
'''
import requests

request_body = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

response = requests.post("https://api.restful-api.dev/objects", json=request_body)
print("response:",response)
status_code = response.status_code
print("response.status_code:",status_code)
response_body = response.json()
print("response.json():",response_body)
object_id = response_body["id"]
print("object_id:", object_id)