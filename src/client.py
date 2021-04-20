#! /usr/bin/env python3
# can recieve files and read but wont close after :(((
import socket, sys, re                   # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = "127.0.0.1"    # Get local machine name
port = 50001                    # Reserve a port for your service.
BUFFER_SIZE = 1024

s.connect((host, port))

filename='mytext.txt'
f = open(filename,'rb')
l = f.read(1024)

while (l):
    s.send(l)
    print('Sent ',repr(l)) #repr returns string containing printable representation of object
    l = f.read(1024)
    f.close()
    break
        

print('Successfully sent the file')
#s.shutdown(socket.SHUT_WR)
#while 1:
 #   data = s.recv(BUFFER_SIZE).decode()
  #  print("Received '%s'" % data)
   # if len(data) == 0:
    #    break
#print("Zero length read.  Closing")
s.close()
print('connection closed')
