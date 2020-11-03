#TCP datetime program
import socket
from datetime import date

today = date.today()

s = socket.socket()
s.bind(('localhost', 9999))

s.listen(1)
print('Server is listening')

c, addr = s.accept()
print('Connected with ', addr)
d = c.recv(1024)
while (True):
    #data = input("Enter message:")
    c.sendall(str(today).encode())
    command = c.recv(1024)
    if command.decode() == "stop":
        break
    elif command.decode() == "continue":
        continue
s.close()


