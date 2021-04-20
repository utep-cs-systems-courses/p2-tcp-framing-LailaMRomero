#! /usr/bin/env python3
#can send files, receive messages
#need to frame the messages
import socket, sys, re                   # Import socket module

port = 50001                    # Reserve a port for your service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
ip = "127.0.0.1"    # Get local machine name
s.bind((ip, port))            # Bind to the port
s.listen(2)                     # Now wait for client connection.
BUFFER_SIZE = 1024

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(BUFFER_SIZE)
    print('Data in file: %s', (data))
    #print('Server received', repr(data))
    
with open('received_file', 'wb') as f:
    print('file opened')
    f.close()
#while True:
 #   print('receiving data...')
   # data = s.recv(BUFFER_SIZE)
  #  print('Data in file: %s', (data))
    #if not data:
                #f.close()
            # print('file close()')
        #break
   # break
        # write data to a file
        #f.w

    #sendMsg = "thanks for connecting %s" % data
    #while len(sendMsg):
     #   bytesSent = conn.send(sendMsg.encode())
      #  sendMsg = sendMsg[bytesSent:0]
conn.shutdown(socket.SHUT_WR)
conn.close()
s.close()
print('Connection closed')
