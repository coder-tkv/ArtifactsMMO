# arangaduy, mark - gathering ash tree
# tkv - fight and rest chickens; craft ash_plank, wooden_shield; recycle wooden_shield

from character_class import Character
import asyncio


async def tkv_run():  # get, craft
    target_ash_wood = 10
    target_ash_planks = 6
    async with Character('tkv') as tkv:
        while True:
            bank = await tkv.get_bank_items()
            count_ash_wood = 0
            for slot in bank:
                if slot['code'] == 'ash_wood':
                    count_ash_wood = slot['quantity']
                    print('ash wood count in bank:', count_ash_wood)
                    break
            if count_ash_wood >= target_ash_wood:
                await tkv.move(4, 1)
                await tkv.withdraw_items('ash_wood', count_ash_wood // target_ash_wood * target_ash_wood)
                await tkv.move(-2, -3)
                for i in range(count_ash_wood // target_ash_wood):
                    await tkv.craft('ash_plank')
                inventory = await tkv.get_inventory()
                count_ash_plank = 0
                for slot in inventory:
                    if slot['code'] == 'ash_plank':
                        count_ash_plank = slot['quantity']
                        print('ash plank count in inventory:', count_ash_plank)
                        break
                if count_ash_plank >= target_ash_planks:
                    await tkv.move(3, 1)
                    while count_ash_plank >= target_ash_planks:
                        await tkv.craft('wooden_shield')
                        await tkv.recycle('wooden_shield', 1)
                        inventory = await tkv.get_inventory()
                        for slot in inventory:
                            if slot['code'] == 'ash_plank':
                                count_ash_plank = slot['quantity']
                                print('ash plank count in inventory:', count_ash_plank)
                                break
            else:
                await tkv.move(0, 1)
                await tkv.fight()
                await tkv.rest()


async def arangaduy_run():  # gathering, put
    target_ash_wood = 5
    async with Character('arangaduy') as arangaduy:
        while True:
            await arangaduy.move(-1, 0)
            inventory = await arangaduy.get_inventory()
            count_ash_wood = 0
            for slot in inventory:
                if slot['code'] == 'ash_wood':
                    count_ash_wood = slot['quantity']
                    print('ash wood count in inventory:', count_ash_wood)
                    break
            if count_ash_wood >= target_ash_wood:
                await arangaduy.move(4, 1)
                await arangaduy.deposit_items('ash_wood', count_ash_wood)
                await arangaduy.move(-1, 0)
            else:
                await arangaduy.gathering()

async def mark_run():  # gathering, put
    target_ash_wood = 5
    async with Character('mark') as mark:
        while True:
            await mark.move(-1, 0)
            inventory = await mark.get_inventory()
            count_ash_wood = 0
            for slot in inventory:
                if slot['code'] == 'ash_wood':
                    count_ash_wood = slot['quantity']
                    print('ash wood count in inventory:', count_ash_wood)
                    break
            if count_ash_wood >= target_ash_wood:
                await mark.move(4, 1)
                await mark.deposit_items('ash_wood', count_ash_wood)
                await mark.move(-1, 0)
            else:
                await mark.gathering()



async def main():
    await asyncio.gather(tkv_run(), arangaduy_run(), mark_run())


asyncio.run(main())
