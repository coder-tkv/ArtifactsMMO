# arangaduy, mark - gathering iron ore
# polina, sonya - gathering spruce tree
# tkv - fight and rest

from character_class import Character
import asyncio


async def tkv_run():  # get
    async with Character('tkv') as tkv:
        await tkv.move(1, -1)
        counter = 0
        sum_of_cooldown_fight = 0
        sum_of_cooldown_rest = 0
        sum_of_xp = 0
        while True:
            fight_result = await tkv.fight()
            sum_of_cooldown_fight += fight_result["cooldown"]["total_seconds"]
            sum_of_xp += fight_result['fight']['xp']
            rest_result = await tkv.rest()
            sum_of_cooldown_rest += rest_result["cooldown"]["total_seconds"]
            counter += 1
            print(f'sum_of_cooldown_fight: {sum_of_cooldown_fight}, '
                  f'sum_of_cooldown_rest: {sum_of_cooldown_rest}, '
                  f'sum_of_xp: {sum_of_xp}, '
                  f'counter: {counter}')
            print(f'average cooldown fights: {sum_of_cooldown_fight / counter}, '
                  f'cooldown rest: {sum_of_cooldown_rest / counter} '
                  f'xp: {sum_of_xp / counter}')


async def arangaduy_run():  # gathering spruce wood, put
    target_wood = 50
    async with Character('arangaduy') as arangaduy:
        while True:
            await arangaduy.move(2, 6)
            inventory = await arangaduy.get_inventory()
            count_spruce_wood = 0
            for slot in inventory:
                if slot['code'] == 'spruce_wood':
                    count_spruce_wood = slot['quantity']
                    print('spruce wood count in inventory:', count_spruce_wood)
                    break
            if count_spruce_wood >= target_wood:
                await arangaduy.move(4, 1)
                await arangaduy.deposit_items('spruce_wood', count_spruce_wood)
                await arangaduy.move(2, 6)
            else:
                await arangaduy.gathering()


async def mark_run():  # gathering spruce wood, put
    target_wood = 50
    async with Character('mark') as mark:
        while True:
            await mark.move(2, 6)
            inventory = await mark.get_inventory()
            count_spruce_wood = 0
            for slot in inventory:
                if slot['code'] == 'spruce_wood':
                    count_spruce_wood = slot['quantity']
                    print('spruce wood count in inventory:', count_spruce_wood)
                    break
            if count_spruce_wood >= target_wood:
                await mark.move(4, 1)
                await mark.deposit_items('spruce_wood', count_spruce_wood)
                await mark.move(2, 6)
            else:
                await mark.gathering()


async def sonya_run():  # gathering iron ore, put
    target_ore = 50
    async with Character('sonya') as sonya:
        while True:
            await sonya.move(1, 7)
            inventory = await sonya.get_inventory()
            count_iron_ore = 0
            for slot in inventory:
                if slot['code'] == 'iron_ore':
                    count_iron_ore = slot['quantity']
                    print('ore count in inventory:', count_iron_ore)
                    break
            if count_iron_ore >= target_ore:
                await sonya.move(4, 1)
                await sonya.deposit_items('iron_ore', count_iron_ore)
                await sonya.move(1, 7)
            else:
                await sonya.gathering()


async def polina_run():  # gathering iron ore, put
    target_ore = 50
    async with Character('polina') as polina:
        while True:
            await polina.move(1, 7)
            inventory = await polina.get_inventory()
            count_iron_ore = 0
            for slot in inventory:
                if slot['code'] == 'iron_ore':
                    count_iron_ore = slot['quantity']
                    print('ore count in inventory:', count_iron_ore)
                    break
            if count_iron_ore >= target_ore:
                await polina.move(4, 1)
                await polina.deposit_items('iron_ore', count_iron_ore)
                await polina.move(1, 7)
            else:
                await polina.gathering()


async def main():
    await asyncio.gather(tkv_run(), arangaduy_run(), mark_run(), sonya_run(), polina_run())


asyncio.run(main())
