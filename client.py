import socket


SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT = "des"


my_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_client.connect(ADDR)

def send_name():
    name = input("enter your name : ")
    name = name.encode(FORMAT)
    name_len = len(name)
    send_len = str(name_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    my_client.send(send_len)
    my_client.send(name)

def send_message(msg):
    msg = msg.encode(FORMAT)
    msg_len = len(msg)
    msg_len = str(msg_len).encode(FORMAT)
    msg_len += b' ' * (HEADER - len(msg_len))
    my_client.send(msg_len)
    my_client.send(msg)



def main():
    connect = True
    while connect:
        try:
            msgs = input("Enter Your Message: ")
            send_message(msgs)
            if msgs == DISCONNECT:
                connect = False
        except KeyboardInterrupt:
            send_message(DISCONNECT)
            connect = False

















send_name()
main()
