
import socket
c = socket.socket(type=socket.SOCK_DGRAM)
c.connect(('localhost',9999))
print('Client waiting for connection')

while(True):
    data = input("Enter message:")
    c.sendto(data.encode(),('localhost',9999))
    msg = c.recvfrom(1024)
    print("Server echoed:"+msg[0].decode())
    if (msg[0].decode() == 'stop'):
        print("Stopping connection")
        break
c.close()