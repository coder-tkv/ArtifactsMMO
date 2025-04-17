import os
import requests
import time


class Character:
    def __init__(self, name):
        self.name = name
        self.API_TOKEN = os.getenv('API_TOKEN')
        self.SERVER = "https://api.artifactsmmo.com"
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            'Authorization': f'Bearer {self.API_TOKEN}'
        }

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

    def move(self, x, y):
        destination_coord = {
            "x": x,
            "y": y
        }
        url = self.SERVER + '/my/' + self.name + '/action/move'
        response = requests.post(url, headers=self.headers, json=destination_coord, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: move to {x}, {y} ---')
        if response.status_code == 200:
            print(f"You arrived at {data['data']['destination']['name']}")
            cooldown = data['data']["cooldown"]["total_seconds"]
            print(f'Cooldown: {cooldown}')
            self.sleep(cooldown)
            return data
        elif response.status_code == 490:
            print('Character already at destination.')
            return data
        else:
            print(f'error : {response.status_code}')
            print(data)
            exit()

    def fight(self):
        url = self.SERVER + '/my/' + self.name + '/action/fight'
        response = requests.post(url, headers=self.headers, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: fight ---')
        if response.status_code == 200:
            print(f"You {data['data']['fight']['result']} the fight!")
            print(f"You win {data['data']['fight']['xp']} Exp points")
            print(f"You win {data['data']['fight']['gold']} Gold")
            for item in data['data']['fight']['drops']:
                print(f"You found {item['quantity']} {item['code']}")
            cooldown = data['data']["cooldown"]["total_seconds"]
            print(f'Cooldown: {cooldown}')
            self.sleep(cooldown)
            return data
        else:
            print(f'error : {response.status_code}')
            print(data)
            exit()

    def rest(self):
        url = self.SERVER + '/my/' + self.name + '/action/rest'
        response = requests.post(url, headers=self.headers, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: rest ---')
        if response.status_code == 200:
            print(f"You are resting")
            print(f'{data['data']['hp_restored']} hp will be restored')
            cooldown = data['data']["cooldown"]["total_seconds"]
            print(f'Cooldown: {cooldown}')
            self.sleep(cooldown)
            return data
        else:
            print(f'error : {response.status_code}')
            print(data)
            exit()

    def gathering(self):
        url = self.SERVER + '/my/' + self.name + '/action/gathering'
        response = requests.post(url, headers=self.headers, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: gathering ---')
        if response.status_code == 200:
            print("Your character successfully gathered the ressource.")
            cooldown = data['data']["cooldown"]["total_seconds"]
            print(f'Cooldown: {cooldown}')
            self.sleep(cooldown)
            return data
        elif response.status_code == 497:
            print("Your character's inventory is full.")
            exit()
        elif response.status_code == 499:
            print("Your character is in cooldown.")
            exit()
        elif response.status_code == 493:
            print("The resource is too high-level for your character.")
            exit()
        else:
            print("An error occured while gathering the ressource.")
            exit()

    def unequip(self, slot='weapon'):
        url = self.SERVER + '/my/' + self.name + '/action/unequip'
        unequip_data = {
            "slot": slot
        }
        response = requests.post(url, headers=self.headers, json=unequip_data, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: unequip {slot} ---')
        if response.status_code == 200:
            print(f'Equipment removed: {slot}')
            cooldown = data['data']["cooldown"]["total_seconds"]
            print(f'Cooldown: {cooldown}')
            self.sleep(cooldown)
            return data
        else:
            print(f'error : {response.status_code}')
            print(data)
            exit()

    def equip(self, slot='weapon', code='wooden_staff'):
        url = self.SERVER + '/my/' + self.name + '/action/equip'
        equip_data = {
            'code': code,
            'slot': slot
        }
        response = requests.post(url, headers=self.headers, json=equip_data, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: equip {slot} {code} ---')
        if response.status_code == 200:
            print(f'Equipment added: {slot} {code}')
            cooldown = data['data']["cooldown"]["total_seconds"]
            print(f'Cooldown: {cooldown}')
            self.sleep(cooldown)
            return data
        else:
            print(f'error : {response.status_code}')
            print(data)
            exit()

    def craft(self, code):
        url = self.SERVER + '/my/' + self.name + '/action/crafting'
        craft_data = {
            'code': code,
        }
        response = requests.post(url, headers=self.headers, json=craft_data, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: craft {code} ---')
        if response.status_code == 200:
            print(f'Created: {code}')
            cooldown = data['data']["cooldown"]["total_seconds"]
            print(f'Cooldown: {cooldown}')
            self.sleep(cooldown)
            return data
        else:
            print(f'error : {response.status_code}')
            print(data)
            exit()

    def deposit_items(self, code='copper_ore', quantity=1):
        url = self.SERVER + '/my/' + self.name + '/action/bank/deposit'
        bank_data = {
            'code': code,
            'quantity': quantity
        }
        response = requests.post(url, headers=self.headers, json=bank_data, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: deposit {quantity} {code},  ---')
        if response.status_code == 200:
            print(f'Deposited: {quantity} {code}')
            cooldown = data['data']["cooldown"]["total_seconds"]
            print(f'Cooldown: {cooldown}')
            self.sleep(cooldown)
            return data
        else:
            print(f'error : {response.status_code}')
            print(data)
            exit()

    def withdraw_items(self, code='copper_ore', quantity=1):
        url = self.SERVER + '/my/' + self.name + '/action/bank/withdraw'
        bank_data = {
            'code': code,
            'quantity': quantity
        }
        response = requests.post(url, headers=self.headers, json=bank_data, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: withdraw {quantity} {code},  ---')
        if response.status_code == 200:
            print(f'Withdraw: {quantity} {code}')
            cooldown = data['data']["cooldown"]["total_seconds"]
            print(f'Cooldown: {cooldown}')
            self.sleep(cooldown)
            return data
        else:
            print(f'error : {response.status_code}')
            print(data)
            exit()

    def deposit_gold(self, quantity=1):
        url = self.SERVER + '/my/' + self.name + '/action/bank/deposit/gold'
        bank_data = {
            'quantity': quantity
        }
        response = requests.post(url, headers=self.headers, json=bank_data, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: deposit {quantity} gold  ---')
        if response.status_code == 200:
            print(f'Deposited gold: {quantity}')
            cooldown = data['data']["cooldown"]["total_seconds"]
            print(f'Cooldown: {cooldown}')
            self.sleep(cooldown)
            return data
        else:
            print(f'error : {response.status_code}')
            print(data)
            exit()

    def withdraw_gold(self, quantity=1):
        url = self.SERVER + '/my/' + self.name + '/action/bank/withdraw/gold'
        bank_data = {
            'quantity': quantity
        }
        response = requests.post(url, headers=self.headers, json=bank_data, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: withdraw {quantity} gold  ---')
        if response.status_code == 200:
            print(f'Withdraw gold: {quantity}')
            cooldown = data['data']["cooldown"]["total_seconds"]
            print(f'Cooldown: {cooldown}')
            self.sleep(cooldown)
            return data
        else:
            print(f'error : {response.status_code}')
            print(data)
            exit()

    def get_inventory(self):
        url = self.SERVER + '/my/characters'
        response = requests.get(url, headers=self.headers, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: get inventory ---')
        if response.status_code == 200:
            inventory = []
            for character in data['data']:
                if character['name'] == self.name:
                    for slot in character['inventory']:
                        if slot['code'] != '':
                            print(slot)
                        inventory.append(slot)
                    print('and empty slots')
            return inventory
        else:
            print(f'error : {response.status_code}')
            print(data)
            exit()

    def get_logs(self):
        url = self.SERVER + '/my/logs'
        response = requests.get(url, headers=self.headers, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: get logs ---')
        if response.status_code == 200:
            print(f'Logs:')
            print(data)
            return data
        else:
            print(f'error : {response.status_code}')
            print(data)
            exit()

    def get_stats(self):
        url = self.SERVER + '/my/characters'
        response = requests.get(url, headers=self.headers, allow_redirects=True)
        data = response.json()
        print(f'--- {self.name}: get stats ---')
        if response.status_code == 200:
            print(f'Stats:')
            print(data)
            return data
        else:
            print(f'error : {response.status_code}')
            print(data)
            exit()


# test farm chickens
if __name__ == '__main__':
    tkv = Character('tkv')
    tkv.move(0, 1)
    while True:
        tkv.fight()
        tkv.rest()
