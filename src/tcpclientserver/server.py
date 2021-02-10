import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('192.168.0.121', 2345))

serverSocket.listen(1)

while True:
    print("Listening for connections...")

    clientSocket, address = serverSocket.accept()
    print(f"Connection with {address} established")

    clientSocket.send("Hello! You are connected to the server!".encode())

    while True:
        msg = clientSocket.recv(1024).decode()
        print("Client typed: " + msg)

        if msg == "Bye":
            clientSocket.send("Server is closing".encode())
            print(f"Server has disconnected from {address}")
            clientSocket.close()
            break

    break
