import csv
import json
from pprint import pprint
import httpx
import os

url = 'https://jsonplaceholder.typicode.com/users'

response = httpx.get(url=url)
response = response.json()

# os.mkdir("users")
os.chdir("users")
for i in response:
    with open(f'{i["username"]}.csv', "w") as f:
        f.write(f"ID: {i['id']}\n")
        f.write(f"NAME: {i['name']}\n")
        f.write(f"USERNAME: {i['username']}\n")
        f.write(f"EMAIL: {i['email']}\n")
        f.write(f"PHONE: {i['phone']}\n")
        f.write(f"WEBSITE: {i['website']}\n")
