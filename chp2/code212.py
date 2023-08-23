import asyncio
from util.util import delay

async def main()->None:
    delay_task = asyncio.create_task(delay(2))

    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print(f'timeouted, is this task canceled: {delay_task.cancelled()}')

asyncio.run(main())