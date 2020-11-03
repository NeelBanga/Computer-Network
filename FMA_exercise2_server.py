#UDP datatime program
import socket

from datetime import date

today = date.today()

s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(('localhost', 9999))

#s.listen(1)
print('Server is listening')

#c, addr = s.accept()
#print('Connected with ', addr)
d = s.recvfrom(1024)
while (True):
    #data = input("Enter message:")
    s.sendto(str(today).encode(),d[1])
    command = s.recvfrom(1024)
    if command[0].decode() == "stop":
        s.close()
        break
    elif command[0].decode() == "continue":
        continue
