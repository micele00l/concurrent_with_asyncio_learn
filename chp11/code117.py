import asyncio
from asyncio import Semaphore
from aiohttp import ClientSession


async def get_url(url: str,
                  semaphore: Semaphore,
                  session: ClientSession):
    print('Waiting to acquire semaphore...')
    async with semaphore:
        print('Acquired semaphore, requesting...')
        respose = await session.get(url)
        print('Finished requesting')
        return respose.status


async def main():
    semaphore = Semaphore(10)
    async with ClientSession() as session:
        tasks = [get_url('http://test.local:6880', semaphore, session)
                 for _ in range(100)]
        await asyncio.gather(*tasks)

asyncio.run(main())
