import socket

client = socket.socket()
client.connect(("localhost",9999))
client.sendall(bytes("This is from Client", 'UTF-8'))
while True:
    in_data = client.recv(1024)
    print("From Server :", in_data.decode())
    out_data = input('Client:')
    client.sendall(bytes(out_data, 'UTF-8'))
    if out_data == 'bye':
        break
client.close()
