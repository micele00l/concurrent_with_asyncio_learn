from util import async_timed, delay


async def positive_integers_async(until: int):
    for integer in range(until):
        await delay(integer)
        yield integer


@async_timed()
async def main():
    async_generator = positive_integers_async(3)
    print(type(async_generator))
    async for number in async_generator:
        print(f'got number {number}')
