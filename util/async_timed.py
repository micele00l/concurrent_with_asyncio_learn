import functools
import time
from typing import Callable, Any


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'start {func} with {args} {kwargs}')
            start = time.time()
            try:
                await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end-start
                print(f'finished {func} in {total} second(s)')
        return wrapped
    return wrapper
