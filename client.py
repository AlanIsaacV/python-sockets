from server import HEADERSIZE
import socket

HEADERSIZE = 9
SERVER = "server"
PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


def send(msg: str) -> None:
    message = msg.encode()
    msg_len = len(message)
    header = f"{msg_len:<{HEADERSIZE}}".encode()
    
    # message = header + message
    client.send(header)
    client.send(message)
    
    print(client.recv(1024).decode())

    # msg_length = len(message)
    # send_length = str(msg_length).encode(FORMAT)
    # send_length += b' ' * (HEADER - len(send_length))

if __name__ == "__main__":
    message = input("Enter your message: ")
    send(message)
