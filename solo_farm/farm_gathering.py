from character_class import Character
import asyncio


async def character_run():
    async with Character('sonya') as character:
        await character.move(2, 0)  # move to ash tree
        while True:
            await character.gathering()


async def main():
    await character_run()


asyncio.run(main())
