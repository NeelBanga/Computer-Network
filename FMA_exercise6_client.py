import socket
from threading import *
from _thread import *

c = socket.socket()
c.connect(("localhost",9999))

class fullDuplex(Thread):
    def __init__(self,conn):
        Thread.__init__(self)
        self.conn = conn
        self.d=0
    def run(self):
        name = current_thread().getName()
        while True:
            try:
                if name == "Sender":
                    data = input("Client: ")

                    if data=="stop":
                        self.conn.close()
                    self.conn.send(data.encode())
                elif name == "Reciever":
                    data = self.conn.recv(1024)

                    if data.decode()=="stop":
                        self.conn.close()
                    print("Server:", data.decode())
            except:
                break

sender = fullDuplex(c)
sender.setName("Sender")

reciever = fullDuplex(c)
reciever.setName("Reciever")

sender.start()
reciever.start()
