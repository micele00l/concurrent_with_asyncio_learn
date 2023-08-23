import asyncio
import aiohttp
from aiohttp import ClientSession
from chp4.fetch_status import fetch_status
from util import async_timed

# @async_timed()
# async def main():
#     urls = ['http://example.com']*100
#     async with ClientSession() as session:
#         status_codes = [await fetch_status(session, url) for url in urls]
#         print(status_codes)


@async_timed()
async def main():
    urls = ['http://example.com','python://example.com']
    async with ClientSession() as session:
        requests = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*requests)
        exceptions = [res for res in results if isinstance(res, Exception) ]
        succ_res = [res for res in results if not isinstance(res, Exception) ]

