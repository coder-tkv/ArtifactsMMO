import aiohttp
import asyncio
import os
import time


class Character:
    def __init__(self, name):
        self.session = None
        self.name = name
        self.API_TOKEN = os.getenv('API_TOKEN')
        self.SERVER = "https://api.artifactsmmo.com"
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            'Authorization': f'Bearer {self.API_TOKEN}'
        }

    @staticmethod
    def get_time():
        return time.strftime("%d.%m - %H:%M:%S", time.localtime())

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def move(self, x, y):
        destination_coord = {
            "x": x,
            "y": y
        }
        url = self.SERVER + '/my/' + self.name + '/action/move'
        try:
            async with self.session.post(url, json=destination_coord, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: move to ({x},{y})  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f"You arrived at {data['data']['destination']['name']}")
                    cooldown = data['data']["cooldown"]["total_seconds"]
                    print(f'Cooldown: {cooldown}')
                    await asyncio.sleep(cooldown)
                    return data['data']
                elif response.status == 490:
                    print('Character already at destination.')
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def fight(self):
        url = self.SERVER + '/my/' + self.name + '/action/fight'
        try:
            async with self.session.post(url, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: fight  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f"You {data['data']['fight']['result']} the fight!")
                    print(f"You win {data['data']['fight']['xp']} Exp points")
                    print(f"You win {data['data']['fight']['gold']} Gold")
                    for item in data['data']['fight']['drops']:
                        print(f"You found {item['quantity']} {item['code']}")
                    cooldown = data['data']["cooldown"]["total_seconds"]
                    print(f'Cooldown: {cooldown}')
                    await asyncio.sleep(cooldown)
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def rest(self):
        url = self.SERVER + '/my/' + self.name + '/action/rest'
        try:
            async with self.session.post(url, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: rest  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f"You are resting")
                    print(f'{data['data']['hp_restored']} hp will be restored')
                    cooldown = data['data']["cooldown"]["total_seconds"]
                    print(f'Cooldown: {cooldown}')
                    await asyncio.sleep(cooldown)
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def gathering(self):
        url = self.SERVER + '/my/' + self.name + '/action/gathering'
        try:
            async with self.session.post(url, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: gathering  |  {self.get_time()}  ---')
                if response.status == 200:
                    print("Your character successfully gathered the resource.")
                    cooldown = data['data']["cooldown"]["total_seconds"]
                    print(f'Cooldown: {cooldown}')
                    await asyncio.sleep(cooldown)
                    return data['data']
                elif response.status == 497:
                    print("Your character's inventory is full.")
                    return None
                elif response.status == 499:
                    print("Your character is in cooldown.")
                    return None
                elif response.status == 493:
                    print("The resource is too high-level for your character.")
                    return None
                else:
                    print("An error occurred while gathering the resource.")
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None
        
    async def unequip(self, slot='weapon'):
        url = self.SERVER + '/my/' + self.name + '/action/unequip'
        unequip_data = {
            "slot": slot
        }
        try:
            async with self.session.post(url, json=unequip_data, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: unequip {slot}  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f'Equipment removed: {slot}')
                    cooldown = data['data']["cooldown"]["total_seconds"]
                    print(f'Cooldown: {cooldown}')
                    await asyncio.sleep(cooldown)
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def equip(self, slot='weapon', code='wooden_staff'):
        url = self.SERVER + '/my/' + self.name + '/action/equip'
        equip_data = {
            'code': code,
            'slot': slot
        }
        try:
            async with self.session.post(url, json=equip_data, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: equip ({slot},{code})  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f'Equipment added: {slot} {code}')
                    cooldown = data['data']["cooldown"]["total_seconds"]
                    print(f'Cooldown: {cooldown}')
                    await asyncio.sleep(cooldown)
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def craft(self, code):
        url = self.SERVER + '/my/' + self.name + '/action/crafting'
        craft_data = {
            'code': code,
        }
        try:
            async with self.session.post(url, json=craft_data, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: craft {code}  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f'Created: {code}')
                    cooldown = data['data']["cooldown"]["total_seconds"]
                    print(f'Cooldown: {cooldown}')
                    await asyncio.sleep(cooldown)
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def deposit_items(self, code='copper_ore', quantity=1):
        url = self.SERVER + '/my/' + self.name + '/action/bank/deposit'
        bank_data = {
            'code': code,
            'quantity': quantity
        }
        try:
            async with self.session.post(url, json=bank_data, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: deposit ({code},{quantity})  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f'Deposited: {quantity} {code}')
                    cooldown = data['data']["cooldown"]["total_seconds"]
                    print(f'Cooldown: {cooldown}')
                    await asyncio.sleep(cooldown)
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def withdraw_items(self, code='copper_ore', quantity=1):
        url = self.SERVER + '/my/' + self.name + '/action/bank/withdraw'
        bank_data = {
            'code': code,
            'quantity': quantity
        }
        try:
            async with self.session.post(url, json=bank_data, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: withdraw ({code},{quantity})  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f'Withdraw: {quantity} {code}')
                    cooldown = data['data']["cooldown"]["total_seconds"]
                    print(f'Cooldown: {cooldown}')
                    await asyncio.sleep(cooldown)
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def deposit_gold(self, quantity=1):
        url = self.SERVER + '/my/' + self.name + '/action/bank/deposit/gold'
        bank_data = {
            'quantity': quantity
        }
        try:
            async with self.session.post(url, json=bank_data, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: deposit {quantity} gold  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f'Deposited gold: {quantity}')
                    cooldown = data['data']["cooldown"]["total_seconds"]
                    print(f'Cooldown: {cooldown}')
                    await asyncio.sleep(cooldown)
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def withdraw_gold(self, quantity=1):
        url = self.SERVER + '/my/' + self.name + '/action/bank/withdraw/gold'
        bank_data = {
            'quantity': quantity
        }
        try:
            async with self.session.post(url, json=bank_data, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: withdraw {quantity} gold  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f'Withdraw gold: {quantity}')
                    cooldown = data['data']["cooldown"]["total_seconds"]
                    print(f'Cooldown: {cooldown}')
                    await asyncio.sleep(cooldown)
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def delete_item(self, code='ash_wood', quantity=1):
        url = self.SERVER + '/my/' + self.name + '/action/delete'
        delete_data = {
            'code': code,
            'quantity': quantity
        }
        try:
            async with self.session.post(url, json=delete_data, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: delete item ({code},{quantity})  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f'Deleted: {quantity} {code}')
                    cooldown = data['data']["cooldown"]["total_seconds"]
                    print(f'Cooldown: {cooldown}')
                    await asyncio.sleep(cooldown)
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None


    async def get_inventory(self):
        url = self.SERVER + '/my/characters'
        try:
            async with self.session.get(url, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: get inventory  |  {self.get_time()}  ---')
                if response.status == 200:
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
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def get_logs(self):
        url = self.SERVER + '/my/logs'
        try:
            async with self.session.get(url, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: get logs  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f'Logs:')
                    print(data['data'])
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def get_stats(self):
        url = self.SERVER + '/my/characters'
        try:
            async with self.session.get(url, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: get stats  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f'Stats:')
                    print(data['data'])
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def get_bank_items(self):
        url = self.SERVER + '/my/bank/items'
        try:
            async with self.session.get(url, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: get bank items  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f'Bank items:')
                    print(data['data'])
                    return data['data']
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None

    async def get_bank_gold(self):
        url = self.SERVER + '/my/bank'
        try:
            async with self.session.get(url, headers=self.headers) as response:
                data = await response.json()
                print(f'---  {self.name}: get bank gold  |  {self.get_time()}  ---')
                if response.status == 200:
                    print(f'Gold in bank: {data["data"]["gold"]}')
                    return data["data"]["gold"]
                else:
                    print(f'error : {response.status}')
                    print(data)
                    return None
        except aiohttp.ClientError as e:
            print(f"POST request failed: {e}")
            return None


# usage example
if __name__ == '__main__':
    async def tkv_run():
        async with Character('tkv') as tkv:
            await tkv.move(0, 1)
            await tkv.fight()
            await tkv.rest()
            await tkv.move(-1, 0)
            await tkv.gathering()
            await tkv.unequip()
            await tkv.equip()
            await tkv.get_inventory()
            await tkv.get_bank_items()
            await tkv.get_bank_gold()


    async def arangaduy_run():
        async with Character('arangaduy') as arangaduy:
            await arangaduy.move(-1, 0)
            await arangaduy.gathering()
            await arangaduy.unequip()
            await arangaduy.equip()
            await arangaduy.move(0, 1)
            await arangaduy.fight()
            await arangaduy.rest()
            await arangaduy.get_inventory()


    async def main():
        await asyncio.gather(tkv_run(), arangaduy_run())


    asyncio.run(main())
