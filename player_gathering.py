import requests
import os
API_TOKEN = os.getenv('API_TOKEN')
SERVER = "https://api.artifactsmmo.com"
CHARACTER = 'arangaduy'

url = SERVER + '/my/' + CHARACTER + '/action/gathering'

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'Authorization': f'Bearer {API_TOKEN}'
}

response = requests.post(url, headers=headers, allow_redirects=True)
print(response.status_code)
if response.status_code == 498:
    print("The character cannot be found on your account.")
elif response.status_code == 497:
    print("Your character's inventory is full.")
elif response.status_code == 499:
    print("Your character is in cooldown.")
elif response.status_code == 493:
    print("The resource is too high-level for your character.")
elif response.status_code != 200:
    print("An error occured while gathering the ressource.")
else:
    data = response.json()["data"]
    print("Your character successfully gathered the ressource.")
    print(f'Cooldown: {data["cooldown"]["total_seconds"]}')