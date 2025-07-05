import socket

s = socket.socket() #ipv6 TCP by default
print("Socket created")

s.bind(('localhost', 9999))
s.listen(3)
print("Waiting for connection")
while True:
    c, add = s.accept()
    name = c.recv(1024).decode()
    print("Connected with ", add, name)
    c.send(bytes("Welcome",'utf-8'))
    c.close()