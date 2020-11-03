#9. UDP Remote Command Execution
import socket
import os
s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(('localhost', 9999))

d = s.recvfrom(1024)
os.system('cmd /c "{}"'.format(d[0].decode()))

s.close()
