#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time

i = 0
while i < 10000:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 发送数据:
    print('send   :', i)
    s.sendto(str(i).encode('utf-8'), ('127.0.0.1', 9999))
    print('receive:', s.recv(1024).decode('utf-8'))
    # 接收数据:
    i += 1
    time.sleep(0.1)
    s.close()