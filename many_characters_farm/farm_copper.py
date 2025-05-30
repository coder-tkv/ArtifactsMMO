# polina, sonya - gathering copper ore
# tkv - fight and rest chickens; craft copper

from character_class import Character
import asyncio


async def tkv_run():  # get, craft
    target_copper_ore = 10
    target_copper = 5
    async with Character('tkv') as tkv:
        while True:
            bank = await tkv.get_bank_items()
            count_copper_ore = 0
            for slot in bank:
                if slot['code'] == 'copper_ore':
                    count_copper_ore = slot['quantity']
                    print('ore count in bank:', count_copper_ore)
                    break
            if count_copper_ore >= target_copper_ore:
                await tkv.move(4, 1)
                await tkv.withdraw_items('copper_ore', count_copper_ore // target_copper_ore * target_copper_ore)
                await tkv.move(1, 5)
                for i in range(count_copper_ore // target_copper_ore):
                    await tkv.craft('copper')
                inventory = await tkv.get_inventory()
                count_copper = 0
                for slot in inventory:
                    if slot['code'] == 'copper':
                        count_copper = slot['quantity']
                        print('copper count in inventory:', count_copper)
                        break
                if count_copper >= target_copper:
                    print('Done')
                    exit()
            else:
                await tkv.move(0, 1)
                await tkv.fight()
                await tkv.rest()


async def polina_run():  # gathering copper ore, put
    target_ore = 5
    async with Character('polina') as polina:
        while True:
            await polina.move(2, 0)
            inventory = await polina.get_inventory()
            count_copper_ore = 0
            for slot in inventory:
                if slot['code'] == 'copper_ore':
                    count_copper_ore = slot['quantity']
                    print('ore count in inventory:', count_copper_ore)
                    break
            if count_copper_ore >= target_ore:
                await polina.move(4, 1)
                await polina.deposit_items('copper_ore', count_copper_ore)
                await polina.move(2, 0)
            else:
                await polina.gathering()


async def sonya_run():  # gathering copper ore, put
    target_ore = 5
    async with Character('sonya') as sonya:
        while True:
            await sonya.move(2, 0)
            inventory = await sonya.get_inventory()
            count_copper_ore = 0
            for slot in inventory:
                if slot['code'] == 'copper_ore':
                    count_copper_ore = slot['quantity']
                    print('ore count in inventory:', count_copper_ore)
                    break
            if count_copper_ore >= target_ore:
                await sonya.move(4, 1)
                await sonya.deposit_items('copper_ore', count_copper_ore)
                await sonya.move(2, 0)
            else:
                await sonya.gathering()


async def main():
    await asyncio.gather(tkv_run(), polina_run(), sonya_run())


asyncio.run(main())
