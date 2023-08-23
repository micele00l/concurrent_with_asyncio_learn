import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed
from chp4.fetch_status import fetch_status

@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [fetch_status(session, 'http://example.com', 4),
                    fetch_status(session, 'http://example.com', 1),
                    fetch_status(session, 'http://example.com', 10)]
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)
