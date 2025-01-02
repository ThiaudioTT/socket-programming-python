import socket
import threading

PORT = 5050
# This gets the current IP address of the server.
# We use this instead of 'localhost' because we want to be able to connect to the server from other devices.
# Localhost is a loopback address that only works on the local machine.
CURR_IP = socket.gethostbyname(socket.gethostname())
ADDR = (CURR_IP, PORT)

# Create a new socket object (AF_INET is the address family for IPv4, SOCK_STREAM is the socket type for TCP connections)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    pass


def start():
    "Starts the server and listens for incoming connections."
    server.listen()

    while True:
        conn, addr = server.accept()

        # Start a new thread for each client that connects to the server
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
