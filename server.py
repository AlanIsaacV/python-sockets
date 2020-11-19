import socket
import threading
import pickle

# HEADERSIZE, RECIVE SIZE OF BUFFER MSG
# THE HEADER ARE THE FIRST ${HEADER} DIGITS OF THE MESSAGE
# if header is 3, maximum size of the buffer can be 999
HEADERSIZE = 9
SERVER = socket.gethostname()
PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))


def handle_client(conn: socket.socket, addr: tuple) -> bool:
    print(f"[ NEW CONNECTION ][ {addr} ]")

    if not (header := conn.recv(HEADERSIZE)):
        print(f"[ {addr} ][ NO MSG ]")
        conn.close()
        return False

    msg_len = int(header)
    message = conn.recv(msg_len).decode()
    
    print(f"[ {addr} ][ MSG LEN ] {msg_len}")
    print(f"[ {addr} ] {message}")

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
