import socket
import threading
import os

PORT = 5050
# This gets the current IP address of the server on linux machines.
# We use this instead of 'localhost' because we want to be able to connect to the server from other devices.
# Localhost is a loopback address that only works on the local machine.
CURR_IP = os.popen("hostname -I").read().split()[0]
ADDR = (CURR_IP, PORT)

# Client will send us the length of the message they are sending us in header.
HEADER_SIZE = 8
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

# Create a new socket object (AF_INET is the address family for IPv4, SOCK_STREAM is the socket type for TCP connections)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.settimeout(120)  # waits for 2 minutes before disconnecting the client

    connected = True
    while connected:
        # TODO: is this best practice?
        msg_length = conn.recv(HEADER_SIZE).decode(FORMAT)
        if not msg_length:
            continue
        msg_length = int(msg_length)

        client_msg = conn.recv(msg_length).decode(FORMAT)
        print(f"[{addr}] {client_msg}")
        if client_msg == DISCONNECT_MSG:
            print(f"[DISCONNECTING] client {addr} has disconnected.")
            connected = False

    conn.close()


def start():
    "Starts the server and listens for incoming connections."
    server.listen()
    print(f"[LISTENING] server is listening on {CURR_IP}")

    while True:
        conn, addr = server.accept()

        # Start a new thread for each client that connects to the server
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()
