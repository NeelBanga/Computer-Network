import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',9999))

#s.listen(1)
print('Server is listening')
tup = s.recv(1024)
addr = tup[1]
#c, addr = s.recv(1024)
print('Connected with ', addr)
t = 0
while(True):
    tup = s.recv(1024)
    d = tup[0]
    addr = tup[1]
    if(d=='bye'):
        break
    if(t==0):
        t = 1
        print(tup)
        s.sendto("Connected".encode(),('localhost',addr))
        continue
    print('2')
    f = open(tup.decode(),'rt')
    data = f.read()
    line = 0
    for l in f:
        line += 1
    words = data.split(" ")
    characters = len(data)
    s1 = str(len(words))+" "+str(characters)+" "+str(line)

    s.sendto(s1.encode(),('localhost',addr))
c.close()