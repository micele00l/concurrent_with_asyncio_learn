import asyncio
from util import async_timed, delay


@async_timed()
async def main():
    delay_times = [3, 3, 3]
    tasks = [asyncio.create_task(delay(sec)) for sec in delay_times]
    [await task for task in tasks]
