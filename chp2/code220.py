import requests
import asyncio
from util import async_timed


@async_timed()
async def get_example_status() -> int:
    return requests.get('https://example.com').status_code


@async_timed()
async def main() -> None:
    task_1 = asyncio.create_task(get_example_status())
    task_2 = asyncio.create_task(get_example_status())
    task_3 = asyncio.create_task(get_example_status())

    await task_1
    await task_2
    await task_3