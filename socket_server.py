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


