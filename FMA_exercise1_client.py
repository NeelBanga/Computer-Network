import socket

c = socket.socket()

c.connect(('localhost',9999))
print('Client waiting for connection')
c.sendall('Client Connected'.encode())
while(True):
    msg = c.recv(1024)
    if (msg.decode() == ''):
        break
    print('Server:'+msg.decode())
    command = input("Enter command to continue or terminate")
    c.sendall(command.encode())

c.close()