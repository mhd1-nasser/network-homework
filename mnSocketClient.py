import socket
ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 3000
print('Please Enter Your Name: ')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)
while True:
    Input = input()
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
ClientMultiSocket.close()