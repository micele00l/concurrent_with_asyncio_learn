import asyncio
from util import delay

def call_later():
    print('i\'m being called in the future')

async def main():
    loop=asyncio.get_running_loop()
    loop.call_soon(callback=call_later)
    await delay(1)