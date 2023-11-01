import asyncio
from asyncio import Transport, Future, AbstractEventLoop, transports
from typing import Optional


class HTTPGetClientProtocal(asyncio.Protocol):

    def __init__(self, host: str, loop: AbstractEventLoop):
        self._host = host
        self._future: Future = loop.create_future()
        self._transport: Optional[Transport] = None
        self._response_buffer: bytes = b''

    async def get_response(self):
        return await self._future

    def _get_requests_bytes(self) -> bytes:
        request = f'GET / HTTP/1.1\r\n' \
            f'Connection: close\r\n' \
            f'Host: {self._host}\r\n\r\n'
        return request.encode()

    def connection_made(self, transport: Transport):
        print(f'Connection made to {self._host}')
        self._transport = transport
        self._transport.write(self._get_requests_bytes())

    def data_receive(self, data):
        print(f'Data received!')
        self._response_buffer += data

    def eof_received(self) -> Optional[bool]:
        self._future.set_result(self._response_buffer.decode())
        return False

    def connection_lost(self, exc: Optional[Exception]) -> None:
        if exc is None:
            print(f'Connection closed without error.')
        else:
            self._future.set_exception(exc)
