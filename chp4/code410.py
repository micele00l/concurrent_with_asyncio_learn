import asyncio
import aiohttp
from aiohttp import ClientSession
from util.async_timed import async_timed
from chp4.fetch_status import fetch_status

@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'http://example.com')),
            asyncio.create_task(fetch_status(session, 'http://example.com'))
        ]

        done, pending = await asyncio.wait(fetchers)
        print(f'done tasks: {len(done)}')
        print(f'pending tasks: {len(pending)}')

        for done_task in done:
            print(await done_task)
