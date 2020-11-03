import socket

c = socket.socket()

c.connect(('localhost',9999))
print('Client waiting for connection')
c.send('Client waiting for conn'.encode())
while(True):
    msg = c.recv(1024)
    if (msg.decode() == 'bye'):
        break
    print('Server:'+msg.decode())
    command = input('Client:')
    c.sendall(command.encode())

c.close()