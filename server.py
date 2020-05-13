import socket
import threading
from user import userr

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT = "des"


users = []

host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host.bind(ADDR)

def begin():
    host.listen()
    print(f"[LISTENING] Server Started Listening on {PORT} .......")
    print("[WAITING] Waiting For Connections .....")
    while True:
        conn, addr = host.accept()
        name_thread = threading.Thread(target=recv_name, args=(conn, addr))
        name_thread.start()


def recv_name(conn, addr):
    name_len = conn.recv(HEADER).decode(FORMAT)
    if name_len:
        name_len = int(name_len)
        name = conn.recv(name_len).decode(FORMAT)
        us_inf = userr(name, addr)
        users.append(us_inf)
        print(f"[JOINING] User {name} Joined The Server......")
        chat_thread = threading.Thread(target=chatting, args=(conn, addr))
        chat_thread.start()


def chatting(conn, addr):
    connected = True

    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            user = get_user(addr)
            print(f"[{user}]: {msg} .")
            if msg == DISCONNECT:
                print(f"[DISCONNECTED] {user} is disconnected .")
                connected = False



def get_user(addrs):
    for i in users:
        if i.addr == addrs:
            user = i.name
            return user














print("[STARTING] Server is starting .......")
begin()
