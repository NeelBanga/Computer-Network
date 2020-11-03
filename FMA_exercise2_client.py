import socket

c = socket.socket(type=socket.SOCK_DGRAM)

c.connect(('localhost',9999))
print('Client waiting for connection')
c.sendto('Client Connected'.encode(),('localhost',9999))
while(True):
    msg = c.recvfrom(1024)
    if (msg[0].decode() == ''):
        break
    print('Server:'+msg[0].decode())
    command = input("Enter command to continue or terminate")
    c.sendto(command.encode(),('localhost',9999))

c.close()
