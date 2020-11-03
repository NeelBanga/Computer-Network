#1. Simple TCP/IP program
import socket

s = socket.socket()
s.bind(('localhost', 9999))

s.listen(1)
print('Server is listening')

c, addr = s.accept()
print('Connected with ', addr)
d = c.recv(1024)
while (True):
    data = input("Enter message:")
    c.sendall(data.encode())
    if(data=="stop"):
        print("Stopping connection")
        break
s.close()