#7. Full Duplex chat
import socket
from threading import *
from _thread import *

s = socket.socket()
s.bind(('localhost',9999))
s.listen(1)
d=0
class fullDuplex(Thread):
    def __init__(self,conn):
        global d
        Thread.__init__(self)
        self.conn = conn
        self.d=0
    def run(self):
        name = current_thread().getName()
        while True:
            try:
                if name == "Sender":
                    data = input("Server: ")

                    if data=="stop":
                        self.conn.close()
                    self.conn.send(data.encode())
                elif name == "Reciever":
                    data = self.conn.recv(1024)

                    if data.decode()=="stop":
                        self.conn.close()
                    print("Client:",data.decode())
            except:
                break


c,addr = s.accept()
sender = fullDuplex(c)
sender.setName("Sender")

reciever = fullDuplex(c)
reciever.setName("Reciever")

sender.start()
reciever.start()