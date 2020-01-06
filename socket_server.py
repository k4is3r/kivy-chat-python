import socket
import select

HEADER_LENGTH = 10

IP = '127.0.0.1'
PORT = 1234

sever_socket =  socket.socket(socket.AF_INET,
                              socket.SOCK_STEAM)


server_socket.setsockpot(socket.SOL_SOCKET,
                         socket.SO_REUSEADDR,
                         1)

server_socket.bind((IP,PORT))


server_socker.listen()

socker_list = [server_socket]

clients = {}

print(f'Listening for conections on {IP}:{PORT}...')

def receive_message(client_socket):
    
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False

        message_length =  int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}

