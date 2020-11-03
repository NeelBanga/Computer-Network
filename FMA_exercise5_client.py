import socket

c = socket.socket()

print('Waiting for connection')

c.connect(('localhost', 9999))

while True:
    data = input('Say Something: ')
    c.send(data.encode())
    if data=="stop":
        break

    msg = c.recv(1024)
    print(msg.decode())

c.close()