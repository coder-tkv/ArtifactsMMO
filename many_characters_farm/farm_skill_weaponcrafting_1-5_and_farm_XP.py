# arangaduy, mark - gathering copper rocks
# tkv - craft copper, copper_dagger; recycle copper_dagger

from character_class import Character
import asyncio


async def tkv_run():  # get, craft
    target_copper_ore = 10
    target_copper = 6
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
                    await tkv.move(2, 1)
                    while count_copper >= target_copper:
                        await tkv.craft('copper_dagger')
                        await tkv.recycle('copper_dagger', 1)
                        inventory = await tkv.get_inventory()
                        for slot in inventory:
                            if slot['code'] == 'copper':
                                count_copper = slot['quantity']
                                print('copper count in inventory:', count_copper)
                                break
            else:
                await tkv.move(0, 1)
                await tkv.fight()
                await tkv.rest()


async def arangaduy_run():  # gathering, put
    target_ore = 5
    async with Character('arangaduy') as arangaduy:
        while True:
            await arangaduy.move(2, 0)
            inventory = await arangaduy.get_inventory()
            count_copper_ore = 0
            for slot in inventory:
                if slot['code'] == 'copper_ore':
                    count_copper_ore = slot['quantity']
                    print('ore count in inventory:', count_copper_ore)
                    break
            if count_copper_ore >= target_ore:
                await arangaduy.move(4, 1)
                await arangaduy.deposit_items('copper_ore', count_copper_ore)
                await arangaduy.move(2, 0)
            else:
                await arangaduy.gathering()

async def mark_run():  # gathering, put
    target_ore = 5
    async with Character('mark') as mark:
        while True:
            await mark.move(2, 0)
            inventory = await mark.get_inventory()
            count_copper_ore = 0
            for slot in inventory:
                if slot['code'] == 'copper_ore':
                    count_copper_ore = slot['quantity']
                    print('ore count in inventory:', count_copper_ore)
                    break
            if count_copper_ore >= target_ore:
                await mark.move(4, 1)
                await mark.deposit_items('copper_ore', count_copper_ore)
                await mark.move(2, 0)
            else:
                await mark.gathering()



async def main():
    await asyncio.gather(tkv_run(), arangaduy_run(), mark_run())


asyncio.run(main())
