import requests
import os
API_TOKEN = os.getenv('API_TOKEN')
SERVER = "https://api.artifactsmmo.com"
CHARACTER = 'arangaduy'

url = SERVER + '/my/' + CHARACTER + '/action/bank/deposit'

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'Authorization': f'Bearer {API_TOKEN}'
}

data = {
    'code': 'copper_ore',
    'quantity': 11
}

response = requests.post(url, headers=headers, json=data, allow_redirects=True)
print(response.json())