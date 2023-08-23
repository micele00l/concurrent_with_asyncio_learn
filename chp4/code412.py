import asyncio
import logging
from aiohttp import ClientSession
from util.async_timed import async_timed
from chp4.fetch_status import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'python://example.com')),
            asyncio.create_task(fetch_status(
                session, 'http://example.com', delay=3)),
            asyncio.create_task(fetch_status(
                session, 'http://example.com', delay=3))
        ]

        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

        print(f'done tasks: {len(done)}')
        print(f'pending tasks: {len(pending)}')

        for done_task in done:
            if not done_task.exception():
                print(done_task.result())
            else:
                logging.error('request got an exception',
                              exc_info=done_task.exception())

        for pending_task in pending:
            pending_task.cancel()
