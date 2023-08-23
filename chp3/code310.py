import asyncio
from asyncio import AbstractEventLoop
import socket
import logging
import signal
from typing import List


async def echo(connection: socket, loop: AbstractEventLoop):
    try:
        while data := await loop.sock_recv(connection, 1024):
            print('got data')
            if data == b'boom\r\n':
                raise Exception('unexcepted network error')
            loop.sock_sendall(connection, data)
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()

echo_tasks = []


async def connection_listener(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, addr = await loop.sock_accept()
        connection.setblocking(False)
        print(f'got connection from {addr}')
        echo_task = asyncio.create_task(echo(connection, loop))
        echo_tasks.append(echo_task)


class GracefullExit(SystemExit):
    pass


def shutdown():
    raise GracefullExit()


async def close_echo_tasks(echo_tasks: List[asyncio.Task]):
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            pass
loop = asyncio.new_event_loop()


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_addr = ('localhost', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_addr)
    server_socket.listen()

    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, signame), shutdown)
    await connection_listener(server_socket, loop)


try:
    loop.run_until_complete(main())
except:
    loop.run_until_complete(close_echo_tasks(echo_tasks))
finally:
    loop.close()
