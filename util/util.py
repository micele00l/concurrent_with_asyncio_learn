import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'before sleep {delay_seconds} secs')
    await asyncio.sleep(delay_seconds)
    print(f'after sleep {delay_seconds} secs')
    return delay_seconds
