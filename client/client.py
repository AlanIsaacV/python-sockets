import socket
import pickle
import json
from os import getenv

# HEADERSIZE, RECIVE SIZE OF BUFFER MSG
# THE HEADER ARE THE FIRST ${HEADER} DIGITS OF THE MESSAGE
# if header is 3, maximum size of the buffer can be 999
HEADERSIZE = 9
SERVER = "server"
PORT = int(getenv('PORT', '5089'))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


def send(msg: object) -> None:
    message = pickle.dumps(msg)
    msg_len = len(message)
    header = f"{msg_len:<{HEADERSIZE}}".encode()
    
    client.send(header)
    client.send(message)
    
    print(client.recv(1024).decode())

if __name__ == "__main__":
    with open('test.json') as f:
        message = json.load(f)

    send(message)
