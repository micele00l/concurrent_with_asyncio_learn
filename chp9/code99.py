import asyncio
import typing
from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocket
from typing import Any


class UserCounter(WebSocketEndpoint):
    encoding = 'text'
    sockets = []

    async def on_connect(self, websocket: WebSocket):
        await websocket.accept
        UserCounter.sockets.append(websocket)

    async def on_disconnect(self, websocket: WebSocket, close_code: int):
        UserCounter.sockets.remove(websocket)

    async def on_receive(self, websocket: WebSocket, data: Any) -> None:
        pass

    async def _send_count(self):
        if len(ct := UserCounter.sockets) > 0:
            count_str = str(ct)
            task_to_socket = {asyncio.create_task(WebSocket.send_text(
                count_str)): websocket for websocket in UserCounter.sockets}

            done, pending = await asyncio.wait(task_to_socket)

            for task in done:
                if task.exception() is not None:
                    if task_name := task_to_socket[task] in UserCounter.sockets:
                        UserCounter.sockets.remove(task_name)


app = Starlette(routes=[WebSocketRoute('/counter', UserCounter)])
