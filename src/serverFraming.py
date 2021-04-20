#! /usr/bin/env python3

# Echo server program

import socket, sys, re, os, threading, _thread
sys.path.append("../lib")
import params
from threading import Thread, Lock
from socketserver import ThreadingMixIn
from framedSocket import frameRecv
switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-?', '--usage'), "usage", False),
    (('-d', '--debug'), "debug", False),
    )

progname = "server"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''       # Symbolic name meaning all available interfaces

debug = paramMap['debug']

if paramMap['usage']:
    params.usage()
mutex = Lock()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bindAddress = ("127.0.0.1", listenPort)
s.bind(bindAddress)
s.listen(10)              # allow only one outstanding request
threads = [] # need to change to set() for mutex
buffer2 = set() # MOVE PLACEMENT
# s is a factory for connected sockets
os.chdir("./serverFiles") #for our transferred files
class ClientThread(Thread):
    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print("New thread started for "+ip+":"+str(port))
    
def checkTransfer(filename):
    global buffer2 #global set that makes sure file is not already attempting be transfered from another client
    canTransfer = False
    if filename in buffer2:
        canTransfer = False
        os.write(1,("file name already in set").encode())
        
    else: #unique filename,add
        canTransfer = True
        buffer2.add(filename)
    return canTransfer

while True:
    #global lock 
    print("Waiting for connection...")
    conn, (addr,port) = s.accept()
    if os.fork() == 0:
        print('Connected successful! Connected to ', (addr,port))
        newthread = ClientThread(addr,port,conn) #create new thread for each client connection 
        newthread.start()
        mutex.acquire()
        threads.append(newthread) # add threads to list
        try:
            print("Waiting for client...") #wait to receive file name and its contents
            fileName, fileData = frameRecv(conn) #start receiving file and its contents
            print("Successfully received data: ", fileName , " from client : ", (addr, port))
            fileName = fileName.decode()
            checkTransfer(fileName)
        except:
            print("Failed data transfer")
            conn.send(("0").encode())#failed to receive
            sys.exit(1)
        mutex.release()
            
        #fileName = fileName.decode()
        try:
            transferFile = open(fileName, "wb") #write in binary mode
            transferFile.write(fileData)
            transferFile.close()
        except:
            print("failed to write to file")
            conn.send(("0").encode())#failed to write
            sys.exit(1)
        for t in threads:
            t.join()
        conn.send(("1").encode())#successfully transfered file
        sys.exit(0)



