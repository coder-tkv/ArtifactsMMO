import requests
import os
import time
API_TOKEN = os.getenv('API_TOKEN')
SERVER = "https://api.artifactsmmo.com"
CHARACTER = 'arangaduy'

url = SERVER + '/my/' + CHARACTER + '/action/gathering'

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'Authorization': f'Bearer {API_TOKEN}'
}

while True:
    response = requests.post(url, headers=headers, allow_redirects=True)
    if response.status_code == 498:
        print("The character cannot be found on your account.")
        break
    elif response.status_code == 497:
        print("Your character's inventory is full.")
        break
    elif response.status_code == 499:
        print("Your character is in cooldown.")
        break
    elif response.status_code == 493:
        print("The resource is too high-level for your character.")
        break
    elif response.status_code != 200:
        print("An error occured while gathering the ressource.")
        break
    else:
        data = response.json()["data"]
        print("Your character successfully gathered the ressource.")
        print(f'Cooldown: {data["cooldown"]["total_seconds"]}')
        time.sleep(data["cooldown"]["total_seconds"])

print('end')
