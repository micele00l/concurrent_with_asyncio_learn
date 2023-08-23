import asyncio
from util import async_timed

@async_timed()
async def cpu_bound_work()->int:
    counter=0
    for _ in range(100000000):
        counter = counter +1
    return counter

async def main()->None:
    task_1 = asyncio.create_task(cpu_bound_work())
    await task_1