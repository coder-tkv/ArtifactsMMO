import requests
import os
import time
API_TOKEN = os.getenv('API_TOKEN')
SERVER = "https://api.artifactsmmo.com"
CHARACTER = 'tkv'

url_rest = SERVER + '/my/' + CHARACTER + '/action/rest'
url_fight = SERVER + '/my/' + CHARACTER + '/action/fight'

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'Authorization': f'Bearer {API_TOKEN}'
}

while True:
    response_fight = requests.post(url_fight, headers=headers, allow_redirects=True)
    if response_fight.status_code == 200:
        data = response_fight.json()
        print(f"You {data['data']['fight']['result']} the fight!")
        print(f"You win {data['data']['fight']['xp']} Exp points")
        print(f"You win {data['data']['fight']['gold']} Gold")
        for item in data['data']['fight']['drops']:
            print(f"You found {item['quantity']} {item['code']}")
        cooldown = data['data']['cooldown']['total_seconds']
        print(f'Fight cooldown: {cooldown}')
        print('------')
    else:
        print(f'error : {response_fight.status_code}')
        break
    time.sleep(cooldown)


    response_rest = requests.post(url_rest, headers=headers, allow_redirects=True)
    if response_rest.status_code == 200:
        data = response_fight.json()
        print(data)
        cooldown = data['data']['cooldown']['total_seconds']
        print(f'Rest cooldown: {cooldown}')
        print('------')
    else:
        print(f'error : {response_rest.status_code}')
        break
    time.sleep(cooldown)

print('end')
