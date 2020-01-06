import socket
import errno
from threading import Thread

HEADER_LENGTH = 10
client_socket = None

# Connects to the server
def connect(ip, port, my_username, error_callback):

    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        
        client_socket.connect((ip, port))
    except Exception as e:
        
        error_callback('Connection error: {}'.format(str(e)))
        return False
    username = my_username.encode('utf-8')
    username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
    client_socket.send(username_header + username)

    return True

def send(message):
    message = message.encode('utf-8')
    message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
    client_socket.send(message_header + message)

def start_listening(incoming_message_callback, error_callback):
    Thread(target=listen, args=(incoming_message_callback, error_callback), daemon=True).start()

