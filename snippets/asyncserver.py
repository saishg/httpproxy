import socket
import asyncio

SERVER_PORT = 8080
BUF_SIZE = 10240

def process_connection(clientsocket, address):
    print(str(clientsocket.recv(BUF_SIZE)))
    clientsocket.close()

async def start_server(future):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), SERVER_PORT))
    serversocket.listen(5)

    while True:
        (clientsocket, address) = serversocket.accept()
        process_connection(clientsocket, address)
    future.set_result('Future is done!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(start_server(future))
    try:
        loop.run_forever()
    finally:
        loop.close()
