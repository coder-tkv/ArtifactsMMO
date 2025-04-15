import requests
import os
API_TOKEN = os.getenv('API_TOKEN')
SERVER = "https://api.artifactsmmo.com"

url = SERVER + '/my/characters'

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'Authorization': f'Bearer {API_TOKEN}'
}

response = requests.get(url, headers=headers, allow_redirects=True)
print(response.json()['data'])

