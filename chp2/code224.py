import asyncio
from time import sleep


def call():
    print('print me')
    sleep(.250)


async def main():
    loop = asyncio.get_event_loop()
    loop.call_soon(call)
    loop.slow_callback_duration = .500
