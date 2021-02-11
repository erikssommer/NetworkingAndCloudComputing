import socket

print("Server")

sock = socket.socket(type=socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 4242))

while True:
    print("Awaiting message")
    data, (addr, port) = sock.recvfrom(1024)
    print("Received: {}:{} Content: {}".format(addr, port, data.decode()))

    if data.decode() == "exit":
        end = "Server is closing"
        print(end)
        sock.sendto(end.encode(), (addr, port))
        sock.close()
        break

    print("Enter reply: ", end = '')
    reply = input()
    sock.sendto(reply.encode(),(addr, port))