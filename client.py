import socket

FORMAT = 'UTF-8'
HOST = '192.168.1.12'    # The remote host
PORT = 8989             # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.send(input('Accion: ').encode(FORMAT))

#no fuk u
