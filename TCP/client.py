import socket

SERV_PORT = 12345
SERV_ADDR = "localhost"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERV_ADDR, SERV_PORT))
print("Connected to server")
input_data = input("Enter data to send to server: ")

client.send(input_data.encode())
print("\nData sent to server")
print(f"Received data from server: {client.recv(1024).decode()}")
