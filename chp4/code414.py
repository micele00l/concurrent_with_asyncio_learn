import asyncio
import logging
from aiohttp import ClientSession
from util.async_timed import async_timed
from chp4.fetch_status import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        pending = [
            asyncio.create_task(fetch_status(session, 'http://example.com')),
            asyncio.create_task(fetch_status(session, 'http://example.com')),
            asyncio.create_task(fetch_status(session, 'http://example.com'))
        ]

        while pending:
            done, pending = await asyncio.wait(
                pending, return_when=asyncio.FIRST_COMPLETED)

            print(f'done tasks: {len(done)}')
            print(f'pending tasks: {len(pending)}')

            for done_task in done:
                print(await done_task)
