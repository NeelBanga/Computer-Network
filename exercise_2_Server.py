import socket

class Bank:
    def __init__(self):
        self.balance = 0
    def withdraw(self,value):
        self.balance -= value
    def deposit(self,value):
        self.balance+= value
    def display(self):
        return(self.balance)

s = socket.socket()
s.bind(('localhost',9999))

s.listen(1)
print('Server is listening')

c, addr = s.accept()
print('Connected with ', addr)
flag = 2
acc = Bank()
while(True):

    d = c.recv(1024)
    if(d.decode()=='bye'):
        break
    if(d.decode()=='Client waiting for conn'):
        c.sendall('Server Connected'.encode())

    if(d.decode()=='display'):
        data = acc.display()
        c.sendall(str(data).encode())

    elif(d.decode().isalpha()):
        c.sendall("Enter value".encode())
        if (d.decode() == 'diposit'):
            flag = 1
        elif(d.decode() == 'withdraw'):
            flag = 0

    elif(d.decode().isnumeric()):
        if(flag == 1):
            acc.deposit(int(d.decode()))
            data = acc.display()
            c.sendall(str(data).encode())
        if(flag == 0):
            acc.withdraw(int(d.decode()))
            data = acc.display()
            c.sendall(str(data).encode())

c.close()