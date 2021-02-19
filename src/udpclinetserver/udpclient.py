import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

some_msg = "something"

while some_msg != "Bye":
    some_msg = input("Write something to the server here (Bye to shut "
                     "down server and exit program): ")

    print("Server is responding...")

    msg_send = some_msg.encode()
    c.sendto(msg_send, ('localhost', 2345))

    data, _ = c.recvfrom(1024)
    msg = data.decode()
    print("Message from server: " + msg)