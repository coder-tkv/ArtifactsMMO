from character_class import Character
import asyncio


async def tkv_run():  # get, craft
    target_ore = 10
    async with Character('tkv') as tkv:
        while True:
            await tkv.move(4, 1)
            bank = await tkv.get_bank_items()
            count_copper_ore = 0
            for slot in bank:
                if slot['code'] == 'copper_ore':
                    count_copper_ore = slot['quantity']
                    print('ore count in bank:', count_copper_ore)
                    break
            if count_copper_ore >= target_ore:
                await tkv.withdraw_items('copper_ore', count_copper_ore)
                await tkv.move(1, 5)
                for i in range(count_copper_ore // 10):
                    await tkv.craft('copper')
                inventory = await tkv.get_inventory()
                count_copper = 0
                for slot in inventory:
                    if slot['code'] == 'copper':
                        count_copper = slot['quantity']
                        print('copper count in inventory:', count_copper)
                        break
                if count_copper >= 6:
                    await tkv.move(2, 1)
                    while count_copper >= 6:
                        await tkv.craft('copper_dagger')
                        await tkv.recycle('copper_dagger', 1)
                        inventory = await tkv.get_inventory()
                        for slot in inventory:
                            if slot['code'] == 'copper':
                                count_copper = slot['quantity']
                                print('copper count in inventory:', count_copper)
                                break
            else:
                await asyncio.sleep(5)


async def arangaduy_run():  # gathering, put
    target_ore = 10
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



async def main():
    await asyncio.gather(tkv_run(), arangaduy_run())


asyncio.run(main())
