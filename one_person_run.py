from character_class import Character
import asyncio


async def character_run():
    async with Character('tkv') as character:
        await character.move(4, 1)
        await character.deposit_items('feather', 19)


async def main():
    await character_run()


asyncio.run(main())
