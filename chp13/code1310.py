import asyncio
from asyncio.subprocess import Process


async def main():
    program = ['python3', 'code139.py']
    process: Process = await asyncio.create_subprocess_exec(*program,
                                                            stdout=asyncio.subprocess.PIPE,
                                                            stdin=asyncio.subprocess.PIPE)

    stdout, stderr = await process.communicate(b'Zoot')
    print(stdout)
    print(stderr)


asyncio.run(main())
