from threading import Thread
import socket


def echo(client: socket.socket):
    while True:
        data = client.recv(2068)
        print(f'Receive {data}, sending!')
        client.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', 8000))
    server.listen()
    while True:
        connection, _ = server.accept()
        thread = Thread(target=echo, args=(connection,))
        thread.start()
