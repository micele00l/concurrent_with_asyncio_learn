import asyncio
from aiohttp import ClientSession
from util.async_timed import async_timed
from chp4.fetch_status import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'http://example.com'
        fetchers = [asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url, delay=3))]

        done, pending = await asyncio.wait(fetchers, timeout=1)

        print(f'done tasks: {len(done)}')
        print(f'pending tasks: {len(pending)}')
        for done_task in done:
            print(await done_task)
        for pendiing_task in pending:
            pendiing_task.cancel()