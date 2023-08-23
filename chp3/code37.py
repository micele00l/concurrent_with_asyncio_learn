import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple
from datetime import datetime

selector = selectors.DefaultSelector()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_addr = ('localhost', 8000)
server_socket.bind(server_addr)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)
    if len(events) == 0:
        now_s = datetime.now().strftime('%H:%M:%S')
        print(f'{now_s} no events, waiting a bit more')
    for event, _ in events:
        event_socket = event.fileobj

        if event_socket == server_socket:
            connection, client_addr = server_socket.accept()
            connection.setblocking(False)
            now_s = datetime.now().strftime('%H:%M:%S')
            print(f'{now_s} i got a connection from {client_addr}')
            selector.register(connection, selectors.EVENT_READ)
        else:
            data = event_socket.recv(1024)
            if len(data) > 0:
                now_s = datetime.now().strftime('%H:%M:%S')
                print(f'{now_s} all data is {data}')
                event_socket.send(data)
