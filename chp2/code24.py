import asyncio


async def coroutine_add_one(number: int) -> int:
    return number+1

async def main() -> None:
    result2 = await coroutine_add_one(1)
    print(result2)

async def main() -> None:
    result1 = await coroutine_add_one(1)
    result2 = await coroutine_add_one(1)
    print(result1)
    print(result2)

asyncio.run(main())