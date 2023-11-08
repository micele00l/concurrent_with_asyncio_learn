import asyncio
from asyncio.subprocess import Process


async def main():
    program = ['python3', 'code134.py']
    process: Process = await asyncio.create_subprocess_exec(*program,
                                                            stdout=asyncio.subprocess.PIPE)
    print(f'Process pid is: {process.pid}')

    return_code = await process.wait()
    print(f'Process returned: {return_code}')


asyncio.run(main())
