from character_class import Character
import asyncio


async def tkv_run():
    async with Character('tkv') as tkv:
        await tkv.move(2, 1)
        await tkv.recycle('copper_dagger', 1)


async def main():
    await asyncio.gather(tkv_run())


asyncio.run(main())
