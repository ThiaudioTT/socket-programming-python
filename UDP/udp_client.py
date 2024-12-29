import socket

SERV_PORT = 12345
SERV_ADDR = "localhost"

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

input_data = input("Enter data to send to server: ")

client.sendto(input_data.encode(), (SERV_ADDR, SERV_PORT))

print("\nData sent to server")

# data, addr = client.recvfrom(1024)
# print(f"Received data from server: {data.decode()}")
