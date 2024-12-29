import socket

# creates server socket

PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", PORT))

server.listen(5)
print(f"Server is listening on port {PORT}")

while True:
    client, addr = server.accept()
    print(f"Received connection from address: {addr} and client: {client}")

    data = client.recv(1024).decode()

    print(f"Received data: {data}")

    print("Sending data back to client")
    client.send(data.encode())
