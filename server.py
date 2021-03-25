#! /usr/bin/env python3

import socket, sys, re                   # Import socket module

port = 50001                    # Reserve a port for your service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = "127.0.0.1"    # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024).decode()
    print('Server received', repr(data))

    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    sendMsg = "thanks for connecting %s" % data
    while len(sendMsg):
        bytesSent = conn.send(sendMsg.encode())
        sendMsg = sendMsg[bytesSent:0]
conn.shutdown(socket.SHUT_WR)
conn.close()
