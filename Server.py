#! /usr/bin/env python3

import re, os, sys
import socket
sys.path.append("../lib")# for params
import params
from FTPSock import *

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "fileServer"
paramMap = params.parseParams(switchesVarDefaults)
debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # listener socket
bindAddr = ("127.0.0.1", listenPort)
lSock.bind(bindAddr)

lSock.listen(1) #listen for a connection
myPrint('Listening in ' + str(bindAddr))

while 1:
    conn, addr = lSock.accept() #accept the connection
    myPrint('Connected to: ' + str(addr))
    ftp_send_Hello(conn)

    try:
        fCont = ftp_recv(conn) #receive connection
        file_name = fCont[:fCont.index('NAME')] #get the filename
        myWrite(file_name, fCont[fCont.index('NAME') + 2:])
        myPrint('Completed file transfer') #Complete message
        break
    except:
        myPrint('Error: File Transfer not accomplished')
        sys.exit(1)
        break
conn.close() #formally close the socket
