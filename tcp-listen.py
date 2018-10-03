#!/usr/bin/env python3

import socket
import datetime

HOST = ''           # '' = Listen on all interfaces.
PORT = 4001         # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    while True:
        # accept connections from outside
        conn, addr = s.accept()
        with conn:
            t = datetime.datetime.now()
            strNow = t.strftime('%Y/%m/%d-%H:%M:%S')
            data = ""
            data = conn.recv(1024)
            if not data:
                break
            conn.close()
            print('{} Connect {} {} bytes'.format(strNow, addr, len(data)))
