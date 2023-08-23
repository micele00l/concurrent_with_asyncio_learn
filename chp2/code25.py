import asyncio


async def return_a_mess() -> str:
    await asyncio.sleep(1)
    return "hello world"


async def main() -> None:
    mess = await return_a_mess()
    print(mess)

asyncio.run(main())
