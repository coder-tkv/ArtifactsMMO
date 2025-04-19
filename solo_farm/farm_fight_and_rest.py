from character_class import Character
import asyncio


async def character_run():
    async with Character('tkv') as character:
        await character.move(1, -1)  # move to yellow slime
        while True:
            await character.fight()
            await character.rest()


async def main():
    await character_run()


asyncio.run(main())
