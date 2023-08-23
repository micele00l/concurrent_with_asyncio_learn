import asyncio
import signal
from asyncio import AbstractEventLoop
from typing import Set

from util import delay

def cancel_task():
    print('got a SIGNAL')
    tasks:Set[asyncio.Task]=asyncio.all_tasks()
    print(f'Cancelling {len(tasks)} task(s)')
    [task.cancel() for task in tasks]

async def main():
    loop:AbstractEventLoop=asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, cancel_task)
    await delay(10)