import socket

s = socket.socket()
s.bind(('localhost',9999))

s.listen(1)
print('Server is listening')

meaning = {
    'nonplussed': 'filled with bewilderment',
    'inchoate': 'only partly in existence',
    'cachet': 'an indication of approved or superior effort',
    'panache': 'distinctive and stylish elegance',
    'indefatigable': 'showing sustained enthusiastic action with unflagging vitality'
}

c, addr = s.accept()
print('Connected with ', addr)
t = 0
while(True):

    d = c.recv(1024)
    if(d.decode()=='bye'):
        break
    if(t == 0):
        c.sendall('Connected'.encode())
        t = 1
        continue

    if(d.decode() in meaning):
        data = meaning[d.decode()]
    else:
        data = "word not found in dictionary"

    c.sendall(data.encode())
c.close()