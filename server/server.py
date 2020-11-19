import socket
import threading
import pickle
import json
from os import getenv

# HEADERSIZE, RECIVE SIZE OF BUFFER MSG
# THE HEADER ARE THE FIRST ${HEADER} DIGITS OF THE MESSAGE
# if header is 3, maximum size of the buffer can be 999
HEADERSIZE = 9
SERVER = socket.gethostname()
PORT = int(getenv('PORT', '5089'))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))


def handle_client(conn: socket.socket, addr: tuple) -> bool:
    print(f"[ NEW CONNECTION ][ {addr} ]")

    if not (header := conn.recv(HEADERSIZE)):
        print(f"[ {addr} ][ NO MSG ]")
        conn.close()
        return False

    msg_len = int(header)
    message = conn.recv(msg_len)
    message = pickle.loads(message)

    print(f"[ {addr} ][ MSG LEN ] {msg_len}")
    print(f"[ {addr} ] {message}")

    with open('from_server.json', 'w') as f:
        json.dump(message, f, ensure_ascii=False)

    conn.send("Message received".encode())
    conn.close()
    return True


def start() -> None:
    server.listen()
    ip = socket.gethostbyname(SERVER)
    print(f"Server listening on on {ip}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))

        thread.start()
        print(f"[ CONNECTIONS ] {threading.active_count() - 1}")


if __name__ == '__main__':
    print("[ STARTING ] Server is starting . . .")
    start()
