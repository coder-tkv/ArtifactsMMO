import requests
import os
API_TOKEN = os.getenv('API_TOKEN')
SERVER = "https://api.artifactsmmo.com"
CHARACTER = 'tkv'

url = SERVER + '/my/' + CHARACTER + '/action/move'

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'Authorization': f'Bearer {API_TOKEN}'
}

data = {
    "x": 0,
    "y": 0
}

response = requests.post(url, headers=headers, json=data, allow_redirects=True)
print(response.json())