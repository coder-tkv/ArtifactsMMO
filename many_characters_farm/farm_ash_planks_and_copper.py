# arangaduy, mark - gathering ash tree
# polina, sonya - gathering ash tree
# tkv - craft ash_plank, craft copper

from character_class import Character
import asyncio


lock = asyncio.Lock()
f_planks = False
f_copper = False


async def tkv_run():  # get
    global f_planks, f_copper

    target_copper = 14
    target_ash_planks = 11

    target_ash_wood = 10
    target_copper_ore = 10
    async with Character('tkv') as tkv:
        while True:
            await tkv.move(4, 1)
            bank = await tkv.get_bank_items()
            count_ash_wood = 0
            count_copper_ore = 0
            for slot in bank:
                if slot['code'] == 'ash_wood':
                    count_ash_wood = slot['quantity']
                    print('ash wood count in bank:', count_ash_wood)
                if slot['code'] == 'copper_ore':
                    count_copper_ore = slot['quantity']
                    print('ore count in bank:', count_copper_ore)
            if count_ash_wood >= target_ash_wood and count_copper_ore >= target_copper_ore:
                await tkv.withdraw_items('copper_ore', count_copper_ore // target_copper_ore * target_copper_ore)
                await tkv.withdraw_items('ash_wood', count_ash_wood // target_ash_wood * target_ash_wood)

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
                    print('Done copper')
                    async with lock:
                        f_copper = True
                    if f_copper and f_planks:
                        exit()

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
                    print('Done planks')
                    async with lock:
                        f_planks = True
                    if f_copper and f_planks:
                        exit()
            elif count_ash_wood >= target_ash_wood:
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
                    print('Done planks')
                    async with lock:
                        f_planks = True
                    if f_copper and f_planks:
                        exit()
            elif count_copper_ore >= target_copper_ore:
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
                    print('Done copper')
                    async with lock:
                        f_copper = True
                    if f_copper and f_planks:
                        exit()
            else:
                await asyncio.sleep(5)


async def arangaduy_run():  # gathering ash wood, put
    global f_planks
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
            if count_ash_wood >= target_ash_wood and not f_planks:
                await arangaduy.move(4, 1)
                await arangaduy.deposit_items('ash_wood', count_ash_wood)
                await arangaduy.move(-1, 0)
            else:
                await arangaduy.gathering()


async def mark_run():  # gathering ash wood, put
    global f_planks
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
            if count_ash_wood >= target_ash_wood and not f_planks:
                await mark.move(4, 1)
                await mark.deposit_items('ash_wood', count_ash_wood)
                await mark.move(-1, 0)
            else:
                await mark.gathering()


async def sonya_run():  # gathering copper, put
    global f_copper
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
            if count_copper_ore >= target_ore and not f_copper:
                await sonya.move(4, 1)
                await sonya.deposit_items('copper_ore', count_copper_ore)
                await sonya.move(2, 0)
            else:
                await sonya.gathering()


async def polina_run():  # gathering copper, put
    global f_copper
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
            if count_copper_ore >= target_ore and not f_copper:
                await polina.move(4, 1)
                await polina.deposit_items('copper_ore', count_copper_ore)
                await polina.move(2, 0)
            else:
                await polina.gathering()


async def main():
    await asyncio.gather(tkv_run(), arangaduy_run(), mark_run(), sonya_run(), polina_run())


asyncio.run(main())
