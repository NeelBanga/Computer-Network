import socket, threading


class ClientThread(threading.Thread):
    def __init__(self, addr, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", addr)
        self.t=0

    def run(self):
        print("Connection from : ", addr)
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if(self.t==0):
                self.csocket.send(bytes('Connected','UTF-8'))
                self.t=1
            else:
                if msg == 'bye':
                    break
                print('From client:',data.decode())
                msg = input('Enter response:')
                self.csocket.send(bytes(msg, 'UTF-8'))
        print("Client at ", addr, " disconnected...")


server = socket.socket()
server.bind(("localhost",9999))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(2)
    c, addr = server.accept()
    newthread = ClientThread(addr, c)
    newthread.start()

