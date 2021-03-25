#! /usr/bin/env python3

import socket
from threading import Thread
from socketserver import ThreadingMixIn

sIP = "127.0.0.1"
sPort = 50001 
BUFFER_SIZE = 1024 #buffer size gives amount to be read in from client

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print("New thread started for "+ip+":"+str(port))

    def run(self):
        filename='mytext.txt'
        f = open(filename,'rb')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #know this one
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #SOL_SOCKET is the level SO_REUSEADDR allows socket to forcibly bind to port in use by another socket with boolean value of true (1)
s.bind((sIP, sPort)) #binding takes the params ip and port and adds info to socket
threads = [] # need to change to set() for mutex

while True:
    s.listen(2)
    print("Waiting for incoming connections...")
    conn, (ip,port) = s.accept() # connects the clients using the ip and ports 
    print ('Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn) #create new thread for each client connection 
    newthread.start()
    threads.append(newthread) # add threads to list
    

for t in threads:
    t.join() # seperates the threads in the list
conn.shutdown(socket.SHUT_WR)
conn.close()
