import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    # ten_millis = aiohttp.ClientTimeout(total=5)
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status
