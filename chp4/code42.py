from aiohttp import ClientSession
from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'http://example.com'
        status = await fetch_status(session, url)
        print(f'status for {url} is {status}')
