import socket
import asyncio
from types import TracebackType
from typing import Optional, Type


class ConnectionSocket:
    def __init__(self, server_socket: socket) -> None:
        self._connection = None
        self._server_socket = server_socket

    async def __aenter__(self) -> socket:
        print('Entering context manager')
        loop = asyncio.get_event_loop()
        self._connection, _ = await loop.sock_accept(self._server_socket)
        return self._connection

    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]):
        print('Exiting context manager')
        self._connection.close()
        print('closed connection')


async def main():
    loop = asyncio.get_event_loop()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_addr = ('localhost', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_addr)
    server_socket.listen()

    async with ConnectionSocket(server_socket) as connection:
        data = await loop.sock_recv(connection, 1024)
        print(f'data is: {data}')