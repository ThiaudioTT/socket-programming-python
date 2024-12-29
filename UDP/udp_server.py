import socket


PORT = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("localhost", PORT))


while True:
    data, addr = server.recvfrom(1024)
    print(f"Received data: {data.decode()} from address: {addr}")

    # print("Sending data back to client")
    # server.sendto(data.encode(), addr)
