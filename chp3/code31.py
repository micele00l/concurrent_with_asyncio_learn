import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_addr = ('localhost', 8000)
server_socket.bind(server_addr)


server_socket.listen()
connection, client_addr = server_socket.accept()
print(f'i got connection from {client_addr}')
