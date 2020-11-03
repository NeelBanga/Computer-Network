import socket

c = socket.socket(type=socket.SOCK_DGRAM)

c.connect(('localhost',9999))

command = input("Enter system command")
c.sendto(command.encode(),('localhost',9999))

c.close()
