#8. File Transfer
import socket
import os

s = socket.socket()
s.bind(('localhost', 9999))

s.listen(1)
print('Server is listening')

c, addr = s.accept()
print('Connected with ', addr)

with open("server_file.txt") as f:

    while True:
        data = f.read(1024)
        if not data:
            print("Stopping Connection")
            break
        c.sendall(data.encode())

f.close()
s.close()