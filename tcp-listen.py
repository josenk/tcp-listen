#!/usr/bin/env python

import socket
import datetime

HOST = ''           # '' = Listen on all interfaces.
PORT = 4001         # Port to listen on (non-privileged ports are > 1023)

try: 
    host_name = socket.gethostname() 
    host_ip = socket.gethostbyname(host_name) 
except: 
    print("Unable to get Hostname and IP") 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
while True:
    # accept connections from outside
    conn, addr = s.accept()
    t = datetime.datetime.now()
    strNow = t.strftime('%Y/%m/%d-%H:%M:%S')
    data = conn.recv(1024)
    conn.send(host_name + " / " + host_ip + "\n")
    conn.close()
    print('{} Connect {} {} bytes'.format(strNow, addr, len(data)))
