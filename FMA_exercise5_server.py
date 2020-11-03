#5. Conccurent clients program
import socket
from _thread import *
import datetime
s = socket.socket()
ThreadCount=0
s.bind(('localhost', 9999))
print('Waitiing for a Connection..')
s.listen(2)

def threaded_client(connection):
    global ThreadCount
    try:
        while True:

            data = connection.recv(1024).decode()
            msg =str(datetime.datetime.now())
            connection.sendall(msg.encode())

            if data=="stop":
                ThreadCount-=1
                print("Threat Number:"+str(ThreadCount))

                if ThreadCount==0:

                        s.close()

    except:
        print("Closing Server")
        connection.close()


try:
    while True:
        c, addr = s.accept()
        print('Connected to: Client',ThreadCount+1)
        start_new_thread(threaded_client, (c, ))
        ThreadCount += 1

        print('Thread Number: ' + str(ThreadCount))
except:
    s.close()

