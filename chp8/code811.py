import asyncio
import asyncpg
import os
import tty
from collections import deque
from asyncpg.pool import Pool
from code85 import create_stdin_reader
from code87 import *
from code88 import read_line
from code89 import MessageStore


async def run_query(query: str, pool: Pool, message_store: MessageStore):
    async with pool.acquire() as connection:
        try:
            result = await connection.fetchrow(query)
            await message_store.append(f'Fetch {len(result)} rows from: {query}')
        except Exception as e:
            message_store.append(f'Got exception {e} from: {query}')


async def main():
    tty.setcbreak(sys.stdin)
    os.system('clear')
    rows = move_to_bottom_of_screen()

    async def redraw_output(items: deque):
        save_cursor_position()
        move_to_top_of_screen()
        for item in items:
            delete_line()
            print(item)
        restore_cursor_position()

    messages = MessageStore(redraw_output, rows - 1)
    stdin_reader = await create_stdin_reader()
    async with asyncpg.create_pool(host='test.local',
                                   port=5432,
                                   user='postgres',
                                   password='password',
                                   database='products',
                                   min_size=6,
                                   max_size=6) as pool:
        while True:
            query = await read_line(stdin_reader)
            asyncio.create_task(run_query(query, pool, messages))

asyncio.run(main())
