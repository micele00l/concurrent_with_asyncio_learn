from threading import Thread
import socket


class ClienEchoThread(Thread):
    def __init__(self, client: socket.socket):
        super().__init__()
        self.client = client

    def run(self):
        try:
            while True:
                data = self.client.recv(2048)
                if not data:
                    raise BrokenPipeError('Connection cloese!')
                print(f'Receive {data}, sending!')
                self.client.sendall(data)
        except OSError as e:
            print(f'Thread interrupted by {e} exception, shutting down!')

    def close(self):
        if self.is_alive():
            self.client.sendall(bytes('Shutting down!', encoding='utf-8'))
            self.client.shutdown(socket.SHUT_RDWR)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', 8000))
    server.listen()
    connection_threads=[]
    while True:
        try:
            connection, _ = server.accept()
            thread = ClienEchoThread(connection)
            connection_threads.append(thread)
            thread.start()
        except KeyboardInterrupt:
            print(f'Shutting down!')
            [t.close() for t in connection_threads]

