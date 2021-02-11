import socket

print("Client")

sock = socket.socket(type=socket.SOCK_DGRAM)
#sock.connect(("localhost", 4242))

while True:
    print("Enter message: ", end='')
    msg = input()
    sock.sendto(msg.encode(), ("localhost", 4242))

    print("Awaiting message")

    reply = sock.recv(1024).decode()
    print("Server replied: {}".format(reply))

    if reply == "Server is closing":
        print("Server is down")
        print("Client is shutting down too")
        break


