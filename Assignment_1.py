import socket

s = socket.socket()
s.bind(('localhost',9999))

s.listen(1)
print('Server is listening')

c, addr = s.accept()
print('Connected with ', addr)

def add1(a,b):
    return a+b

arr = []
t = 0

while(True):

    d = c.recv(1024)
    if(t==0):
        c.sendall('Connected'.encode())
        t = 1
    if(d.decode()=='add'):
        c.sendall('Give first numbers'.encode())
    elif(d.decode().isnumeric()):
        arr.append(int(d.decode()))
        if(len(arr)==1):
            c.sendall('Give second number'.encode())
    if(len(arr)==2):
        data = add1(arr[0],arr[1])
        c.sendall(str(data).encode())
        arr = []
    if(d.decode()=='bye'):
        break

c.close()

