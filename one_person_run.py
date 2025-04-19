from character_class import Character
import asyncio


async def character_run():
    async with Character('tkv') as character:
        await character.rest()


async def main():
    await character_run()


asyncio.run(main())
