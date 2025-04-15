import requests
import os
API_TOKEN = os.getenv('API_TOKEN')
SERVER = "https://api.artifactsmmo.com"
CHARACTER = 'tkv'

url = SERVER + '/my/' + CHARACTER + '/action/crafting'

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'Authorization': f'Bearer {API_TOKEN}'
}

data = {
    'code': 'wooden_staff'
}

response = requests.post(url, headers=headers, json=data, allow_redirects=True)
print(response.json())