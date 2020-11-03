import socket

s = socket.socket()
s.bind(('localhost',9999))

s.listen(1)
print('Server is listening')

c, addr = s.accept()
print('Connected with ', addr)
while(True):

    d = c.recv(1024)
    if(d.decode()=='bye'):
        break
    if(d.decode().isnumeric()):
        data = int(d.decode())**2
    else:
        data = d.decode()
    c.sendall(str(data).encode())
c.close()