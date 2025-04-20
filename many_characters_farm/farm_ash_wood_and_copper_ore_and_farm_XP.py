# arangaduy, mark - gathering ash tree
# polina, sonya - gathering ash tree
# tkv - fight and rest

from character_class import Character
import asyncio


async def tkv_run():  # get
    async with Character('tkv') as tkv:
        await tkv.move(1, -1)
        while True:
            await tkv.fight()
            await tkv.rest()


async def arangaduy_run():  # gathering ash wood, put
    async with Character('arangaduy') as arangaduy:
        await arangaduy.move(-1, 0)
        while True:
            await arangaduy.gathering()


async def mark_run():  # gathering ash wood, put
    async with Character('mark') as mark:
        await mark.move(-1, 0)
        while True:
            await mark.gathering()


async def sonya_run():  # gathering copper, put
    async with Character('sonya') as sonya:
        await sonya.move(2, 0)
        while True:
            await sonya.gathering()


async def polina_run():  # gathering copper, put
    async with Character('polina') as polina:
        await polina.move(2, 0)
        while True:
            await polina.gathering()


async def main():
    await asyncio.gather(tkv_run(), arangaduy_run(), mark_run(), sonya_run(), polina_run())


asyncio.run(main())
