# arangaduy, mark - gathering iron ore
# polina, sonya - gathering spruce tree
# tkv - craft iron and spruce

from character_class import Character
import asyncio


async def tkv_run():  # get
    async with Character('tkv') as tkv:
        while True:
            await tkv.move(4, 1)

            inventory = await tkv.get_inventory()
            copper_counter = 0
            ash_counter = 0
            for slot in inventory:
                if slot['code'] == 'copper':
                    copper_counter = slot['quantity']
                    print('copper count in inventory:', copper_counter)
                if slot['code'] == 'ash_plank':
                    ash_counter = slot['quantity']
                    print('ash plank count in inventory:', ash_counter)

            await tkv.withdraw_items('copper_ore', 60 - copper_counter * 10)
            await tkv.withdraw_items('ash_wood', 60 - ash_counter * 10)

            await tkv.move(1, 5)
            for _ in range((60 - copper_counter * 10) // 10):
                await tkv.craft('copper')

            await tkv.move(-2, -3)
            for _ in range((60 - ash_counter * 10) // 10):
                await tkv.craft('ash_plank')

            await tkv.move(2, 1)
            await tkv.craft('copper_dagger')
            await tkv.recycle('copper_dagger', 1)


            await tkv.move(3, 1)
            await tkv.craft('wooden_shield')
            await tkv.recycle('wooden_shield', 1)


async def arangaduy_run():  # craft spruce plank
    async with Character('arangaduy') as arangaduy:
        while True:
            await arangaduy.move(4, 1)
            await arangaduy.withdraw_items('spruce_wood', 100)

            await arangaduy.move(-2, -3)
            for _ in range(10):
                await arangaduy.craft('spruce_plank')

            await arangaduy.move(4, 1)
            await arangaduy.deposit_items('spruce_plank', 10)


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
                for slot in inventory:
                    if slot['code'] != '' and slot['quantity'] > 5:
                        await mark.deposit_items(slot['code'], slot['quantity'])
                await mark.move(2, 6)
            else:
                await mark.gathering()


async def sonya_run():  # craft iron
    async with Character('sonya') as sonya:
        while True:
            await sonya.move(4, 1)
            await sonya.withdraw_items('iron_ore', 100)

            await sonya.move(1, 5)
            for _ in range(10):
                await sonya.craft('iron')

            await sonya.move(4, 1)
            await sonya.deposit_items('iron', 10)


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
                for slot in inventory:
                    if slot['code'] != '' and slot['quantity'] > 3:
                        await polina.deposit_items(slot['code'], slot['quantity'])
                await polina.move(1, 7)
            else:
                await polina.gathering()


async def main():
    await asyncio.gather(arangaduy_run(), sonya_run(), polina_run(), mark_run(), tkv_run())


asyncio.run(main())
