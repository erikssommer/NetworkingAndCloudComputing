import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('192.168.1.12', 2345))

serverSocket.listen(1)

while True:
    print("Listening for connections...")

    clientSocket, address = serverSocket.accept()
    print(f"Connection with {address} established")

    clientSocket.send("Hello! You are connected to the server. Bye!".encode())

    clientSocket.close()
