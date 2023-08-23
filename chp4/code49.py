import asyncio
from aiohttp import ClientSession
from util.async_timed import async_timed
from chp4.fetch_status import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [fetch_status(session, 'http://example.com', 1),
                    fetch_status(session, 'http://example.com', 1),
                    fetch_status(session, 'http://example.com', 10)]
        for finished_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                print(await finished_task)
            except asyncio.TimeoutError:
                print('we got timeout error')

        for task in asyncio.tasks.all_tasks():
            print(task)
