#!/bin/env/python3

import socketserver

global HOST, PORT
class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).decode("ASCII").strip()
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        self.request.sendall(data)


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 9999
    try:
        with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
            server.serve_forever()
    except KeyboardInterrupt or IOError:
        server.shutdown()
