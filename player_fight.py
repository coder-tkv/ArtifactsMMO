import requests
import os
API_TOKEN = os.getenv('API_TOKEN')
SERVER = "https://api.artifactsmmo.com"
CHARACTER = 'tkv'

url = SERVER + '/my/' + CHARACTER + '/action/fight'

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'Authorization': f'Bearer {API_TOKEN}'
}

response = requests.post(url, headers=headers, allow_redirects=True)
data = response.json()
if response.status_code == 200:
    print(f"You {data['data']['fight']['result']} the fight!")
    print(f"You win {data['data']['fight']['xp']} Exp points")
    print(f"You win {data['data']['fight']['gold']} Gold")
    for item in data['data']['fight']['drops']:
        print(f"You found {item['quantity']} {item['code']}")
else:
    print(f'error : {response.status_code}')