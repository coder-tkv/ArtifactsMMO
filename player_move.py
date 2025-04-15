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

destination_coord = {
    "x": 0,
    "y": 1
}

response = requests.post(url, headers=headers, json=destination_coord, allow_redirects=True)
if response.status_code == 200:
    data = response.json()
    print(f"You arrived at {data['data']['destination']['name']}")
    print(f"The place look like {data['data']['destination']['skin']}")
    print(f"The place contains {data['data']['destination']['content']['code']}")
else:
    print(f'erreur : {response.status_code}')