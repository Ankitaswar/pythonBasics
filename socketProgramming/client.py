import socket

c = socket.socket()
c.connect(('localhost', 9999))
name = "Ankit"
c.send(bytes(name, 'utf-8'))
print(c.recv(1024).decode())