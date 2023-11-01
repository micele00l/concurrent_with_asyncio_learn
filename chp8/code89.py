from collections import deque
from typing import Callable, Deque, Awaitable


class MessageStore:
    def __init__(self, callback: Callable[[Deque], Awaitable[None]], maxsize: int):
        self._deque = deque(maxlen=maxsize)
        self._callback = callback

    async def append(self, item):
        self._deque.append(item)
        await self._callback(self._deque)
