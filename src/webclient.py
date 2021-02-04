import socket

hostname = 'www.ismycomputeron.com'
port = 80

request_lines = [
    "GET / HTTP/1.1",
    "Host: ismycomputeron.com",
    "Connection: close"
]

def make_request(lines):
    return ("\r\n".join(lines))+"\r\n\r\n"

request = make_request(request_lines)

print("Sending request: \"{}\" \n".format(request))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))
s.sendall(request.encode())

data = s.recv(1024)

print("Received: \"{}\"".format(data.decode()))
