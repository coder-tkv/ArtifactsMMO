from character_class import Character
import asyncio


async def character_run():
    async with Character('tkv') as character:
        await character.deposit_items('raw_chicken', 24)


async def main():
    await character_run()


asyncio.run(main())
