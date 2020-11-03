import socket

s = socket.socket()
s.bind(('localhost',9999))

s.listen(1)
print('Server is listening')

c, addr = s.accept()
print('Connected with ', addr)
t = 0
while(True):
    d = c.recv(1024)
    if(d.decode()=='bye'):
        break
    if(t==0):
        t = 1
        c.sendall("Connected".encode())
        continue
    f = open(d.decode(),'rt')
    data = f.read()
    words = data.split()
    c.sendall(str(len(words)).encode())
c.close()