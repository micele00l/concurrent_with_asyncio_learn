from asyncio import Future
import asyncio


async def make_request() -> Future:
    my_f = Future()
    asyncio.create_task(set_future_value(my_f))
    return my_f


async def set_future_value(future: Future) -> None:
    asyncio.sleep(1)
    future.set_result(42)


async def main() -> None:
    ff = make_request()
    print(f'is my future done? {ff.done()}')
    value = await ff
    print(f'is my future done? {ff.done()}')
    print(f'my_future result is {value}')

asyncio.run(main())
