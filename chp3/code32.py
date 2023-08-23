import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_addr = ('localhost', 8000)
server_socket.bind(server_addr)
server_socket.listen()
    
try:
    connection, client_addr = server_socket.accept()
    print(f'i got a connection from {client_addr}')
    buffer = b''
    while buffer[-2:] != b'\r\n':
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f'data is {data}')
            buffer += data
    print(f'all the data is: {buffer}')
    connection.sendall(b'hello '+buffer)
finally:
    server_socket.close()
