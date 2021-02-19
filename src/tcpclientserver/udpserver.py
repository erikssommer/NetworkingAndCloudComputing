import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 2345))

while True:
    data, source = s.recvfrom(1024)
    msg = data.decode()
    print("Message from client: " + msg)

    if data.decode() == "Bye":
        notify_shutdown = "Bye - server shutting down...".encode()
        s.sendto(notify_shutdown, source)
        break

    some_smg = input("Write something to the client: ")
    msg_send = some_smg.encode()
    s.sendto(msg_send, source)
    print("Client is responding...")