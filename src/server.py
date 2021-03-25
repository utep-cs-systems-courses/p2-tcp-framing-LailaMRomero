#! /usr/bin/env python3
#can send files, receive messages
import socket, sys, re                   # Import socket module

port = 50001                    # Reserve a port for your service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
ip = "127.0.0.1"    # Get local machine name
s.bind((ip, port))            # Bind to the port
s.listen(2)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024).decode() #recv and decode bytes
    print('Server received', repr(data))

    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l)) #repr returns string containing printable representation of object
       l = f.read(1024)
       break
    f.close()
    break

    #sendMsg = "thanks for connecting %s" % data
    #while len(sendMsg):
     #   bytesSent = conn.send(sendMsg.encode())
      #  sendMsg = sendMsg[bytesSent:0]
conn.shutdown(socket.SHUT_WR)
conn.close()
s.close()
print('Connection closed')
