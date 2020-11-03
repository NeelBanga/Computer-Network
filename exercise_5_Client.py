import socket

c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

c.connect(('localhost',9999))
print('Client waiting for connection')
c.send('Client waiting for conn'.encode())
while(True):
    msg = c.recv(1024)
    if (msg.decode() == 'bye'):
        break
    if(msg.decode()=="Connected"):
        print("server: Connected")
        continue
    info = msg.decode().split(" ")
    print('Word:',msg[0])
    print('Character',msg[1])
    print('lines',msg[2])
    name = input('Client:')
    c.sendall(name.encode())

c.close()