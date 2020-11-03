#4. UDP echo program
import socket

s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(('localhost', 9999))
print('Server is listening')
while (True):
    d=s.recvfrom(1024)
    if(d=="stop"):
        print("Stopping connection")
        break
    s.sendto(d[0],d[1])
s.close()