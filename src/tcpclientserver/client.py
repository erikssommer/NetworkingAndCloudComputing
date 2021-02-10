import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(('192.168.0.121', 2345))

msg = clientSocket.recv(1024)

print(msg.decode())

while True:
    print("Type input: ", end = '')
    cliInput = input()
    clientSocket.send(cliInput.encode())

    if cliInput == "Bye":
        print(clientSocket.recv(1024).decode())
        break