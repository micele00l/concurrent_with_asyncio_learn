import asyncio
from util import async_timed


@async_timed()
async def delay(delay_num: int) -> int:
    print(f'start sleeping for {delay_num}')
    await asyncio.sleep(delay_num)
    print(f'finished sleeping')
    return delay_num


@async_timed()
async def main():
    task_two = asyncio.create_task(delay(2))
    task_three = asyncio.create_task(delay(3))

    await task_two
    await task_three

asyncio.run(main())
