#!/bin/env/python3

import socket
import sys
import time as t
# from SwipeDown.SwipeDown import swipedown as sd
import shell_server as shellserv

global HOST, port


def shell(host=shellserv.HOST, port=shellserv.PORT):
    data = ' '.join(sys.argv[1:])
    t.sleep(5000)
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host, port))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print("Sent:     {}".format(data))
        print("Received: {}".format(received))
        sock.shutdown(__how=socket.SHUT_RDWR)
