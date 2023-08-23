import asyncio
from aiohttp import ClientSession
from util.async_timed import async_timed
from chp4.fetch_status import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        api_a = fetch_status(session, 'http://example.com')
        api_b = fetch_status(session, 'http://example.com', delay=2)

        done, pending = await asyncio.wait([api_a, api_b], timeout=1)

        print(f'done tasks: {len(done)}')
        print(f'pending tasks: {len(pending)}')

        for pending_task in pending:
            if pending_task is api_b:
                print('api b too slow, cancelling')
                pending_task.cancel()
