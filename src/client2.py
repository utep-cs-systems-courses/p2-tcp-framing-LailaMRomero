#!/usr/bin/env python3

import socket

ip = "127.0.0.1"
port = 50001 
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
with open('received_file', 'wb') as f: #open file as writable
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(BUFFER_SIZE) #receive file in set amounts of bytes
        print('Data in file: %s', (data)) #print data in file
        if not data:
            f.close()
            print('file close()')
            break
        # write data to a file
        #f.write(data)

print('Successfully got the file')
s.close()
print('Connection closed')
