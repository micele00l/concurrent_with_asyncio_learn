import asyncio
from util.util import delay

async def sleep_every_sec(times)->None:
    for _ in range(times):
        print('befor sleep every')
        await asyncio.sleep(1)
        print('running other code while waitting')

async def main() -> None:
    sleep_1 = asyncio.create_task(delay(3))
    sleep_2 = asyncio.create_task(delay(3))

    await sleep_every_sec(2)
    await sleep_1
    await sleep_2

asyncio.run(main())
