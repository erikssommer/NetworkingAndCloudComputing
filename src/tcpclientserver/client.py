import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(('192.168.0.121', 2345))

msg = clientSocket.recv(1024)

print(msg.decode())