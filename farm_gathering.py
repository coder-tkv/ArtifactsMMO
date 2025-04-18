from character_class import Character
import asyncio

async def arangaduy_run():
    async with Character('arangaduy') as arangaduy:
        await arangaduy.move(-1, 0)  # move to ash tree
        while True:
            await arangaduy.gathering()


async def main():
    await arangaduy_run()


asyncio.run(main())
