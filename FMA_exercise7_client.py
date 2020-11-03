import socket
c = socket.socket()
c.connect(('localhost',9999))
print('Client waiting for connection')
f = open("new_file.txt","w")
while True:
    msg = c.recv(1024).decode()

    f.write(msg)
    if msg=='':
        break

f.close()
f = open("new_file.txt","r")
print(f.read())
f.close()
c.close()