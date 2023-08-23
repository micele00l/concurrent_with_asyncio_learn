import asyncio
import socket
from asyncio import AbstractEventLoop
import logging


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    try:
        while data := await loop.sock_recv(connection, 1024):
            if data == b'boom\r\n':
                raise Exception('unexpected network error')
            await loop.sock_sendall(connection, data)
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()


async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, addr = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'i got a connect from {addr}')
        await asyncio.create_task(echo(connection, loop))


async def main() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_addr = ('localhost', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_addr)
    server_socket.listen()

    await listen_for_connection(server_socket, asyncio.get_event_loop())
