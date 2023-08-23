import asyncio
from asyncio import CancelledError
from util.util import delay


async def main() -> None:
    long_task = asyncio.create_task(delay(4))
    sec_elapsed = 0

    while not long_task.done():
        print('task not finish, check again in 1s')
        await asyncio.sleep(1)
        sec_elapsed += 1

        if sec_elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print('task canceled')

asyncio.run(main())
