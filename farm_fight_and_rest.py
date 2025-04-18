from character_class import Character
import asyncio

async def tkv_run():
    async with Character('tkv') as tkv:
        await tkv.move(0, 1)  # move to chickens
        while True:
            await tkv.fight()
            await tkv.rest()


async def main():
    await tkv_run()


asyncio.run(main())
