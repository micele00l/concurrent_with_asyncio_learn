import asyncio
from util.util import delay

async def main()->None:
    delay_task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(delay_task), timeout=3)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print(f'task took timeouted,')
        result = await delay_task
        print(result)

asyncio.run(main())