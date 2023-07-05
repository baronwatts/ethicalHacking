#!/usr/bin/python3
#this code demonstrates a multiport banner­grabbing tool

import socket

Ports = [21,22,25,3306]


for i in range(0,4):
  s = socket.socket()
  Port = Ports[i]
  print('This Is the Banner for the Port')
  print(Port)
  s.connect(("192.185.52.223",Port))
  answer = s.recv(1024)
  print(answer)
s.close();