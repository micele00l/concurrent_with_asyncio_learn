import asyncio
import logging
from aiohttp import ClientSession
from util.async_timed import async_timed
from chp4.fetch_status import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        good_request = fetch_status(session, 'http://example.com')
        bad_request = fetch_status(session, 'python://example.com')
        fetchers = [
            asyncio.create_task(good_request),
            asyncio.create_task(bad_request)
        ]

        done, pending = await asyncio.wait(fetchers)
        print(f'done tasks: {len(done)}')
        print(f'pending tasks: {len(pending)}')

        for done_task in done:
            if not done_task.exception():
                print(done_task.result())
            else:
                logging.error('got request exception',
                              exc_info=done_task.exception())
