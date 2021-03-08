#! /usr/bin/env python3
'''

The Client will send a file that the server must copy, the name
is then attaned from either one
'''
import socket, sys, re
sys.path.append("../lib")# for params
import params
from FTPSock import * #holds file transfer protocol

switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-d', '--debug'), "debug", False), 
    (('-?', '--usage'), "usage", False), 
    )
progname = 'FTPClient'
paramMap = params.parseParams(switchesVarDefaults)

server, usage, debug  = paramMap["server"], paramMap["usage"], paramMap["debug"]

if usage:
    params.usage()

try:
    serverHost, serverPort = re.split(':', server) #attain ip and port #
    serverPort = int(serverPort) #type cast
except: #error case
    pass
    myPrint('Cannot parse server:port from %s' %server)

addrFamily = socket.AF_INET #IPV4
socktype = socket.SOCK_STREAM #TCP COnnection
addrPort = (serverHost, serverPort) #tuple of server

s = socket.socket(addrFamily, socktype) #create the socket

if s is None: #in case socket could not be made
    myPrint('Could not open socket')
    sys.exit(1)

try: #establish connection
    s.connect(addrPort)
    rcMsg = ftp_recv(s) #receive welcome message
    if 'hello' in rcMsg.lower(): #hello message
        myPrint(rsMsg)

    fCopy = readLine() #file to copy
    fNewName = readLine() #new name for the file
    myPrint('Sending file Contents')

    ftp_send(s, fNewName, fCopy) 

except:
        myPrint('Could not connect to the server')
        sys.exit(1)
