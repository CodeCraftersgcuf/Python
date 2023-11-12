import socket

# Constants
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.56.1"  # Replace with your server's IP
ADDR = (SERVER, PORT)

# Create the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

while True:
    msg = input("Enter your message: ")
    if msg == DISCONNECT_MESSAGE:
        break
    send(msg)

client.close()