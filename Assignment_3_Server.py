import socket

s = socket.socket()
s.bind(('localhost',9999))

s.listen(1)
print('Server is listening')

c, addr = s.accept()
print('Connected with ', addr)
t = 0
data = ''
while(True):
    d = c.recv(1024)
    if(t==0):
        c.sendall('connected'.encode())
        t = 1
    elif(d.decode()=='ping'):
        data = 'pong'
    elif(d.decode()=='bye'):
        break
    else:
        data = 'dropped'
    c.sendall(data.encode())
c.close()

