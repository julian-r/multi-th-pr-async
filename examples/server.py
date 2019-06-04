import asyncio

async def handle_echo(reader, writer):
    handle_echo.connection_count  += 1
    print('got connection', handle_echo.connection_count)
    data = await reader.read(100)
    message = data.decode()

handle_echo.connection_count = 0

def aio_main():
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_echo, '127.0.0.1', 1234, loop=loop)
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

import socket
import threading

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.connection_count = 0

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, sock, address):
        self.connection_count += 1
        print('got connection', self.connection_count)
        while True:
            try:
                data = sock.recv(1024)
            except ConnectionResetError:
                print('Client disconnected')
                return
            if data:
                # print(data)
                # Set the response to echo back the recieved data 
                #sock.send(data)
                pass
            else:
                print('Client disconnected')
                return

        sock.close()

def threading_main():
    ThreadedServer('',1234).listen()

if __name__ == "__main__":
    # threading_main()
    aio_main()