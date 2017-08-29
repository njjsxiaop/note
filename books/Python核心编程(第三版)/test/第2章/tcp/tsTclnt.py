#!/usr/bin/env python

from socket import *

HOST = '127.0.0.1' # or 'localhost'
PORT = 21567
BUFSZIE = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSZIE).decode()
    if not data:
        break
    print(data)

tcpCliSock.close()
