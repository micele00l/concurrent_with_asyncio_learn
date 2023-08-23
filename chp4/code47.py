import asyncio
from util import delay


async def main():
    results = await asyncio.gather(delay(1), delay(4))
    print(results)
