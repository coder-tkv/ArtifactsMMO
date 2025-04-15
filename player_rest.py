import requests
import os
API_TOKEN = os.getenv('API_TOKEN')
SERVER = "https://api.artifactsmmo.com"
CHARACTER = 'tkv'

url = SERVER + '/my/' + CHARACTER + '/action/rest'

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'Authorization': f'Bearer {API_TOKEN}'
}

response = requests.post(url, headers=headers, allow_redirects=True)
print(response.json())
