import asyncio
from util import delay

async def add_one(num:int)->int:
    return num+1

async def hello_mess()->str:
    await delay(1)
    return 'hello world'

async def main()->None:
    mess = await hello_mess()
    one_plus = await add_one(1)
    print(mess)
    print(one_plus)

asyncio.run(main())
