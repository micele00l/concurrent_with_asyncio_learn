import asyncio
from util import async_timed

@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for _ in range(100000000):
        counter += 1
    return counter


@async_timed()
async def main() -> None:
    task_ont = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    
    await task_ont
    await task_two
