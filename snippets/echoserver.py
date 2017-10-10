import asyncio
import functools
import logging
import sys

SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s: %(message)s',
        stream=sys.stderr,
        )
log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()

class EchoServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log = logging.getLogger(
            'Echo server {} {}'.format(*self.address)
        )
        self.log.debug('Connection accepted')

    def data_received(self, data):
        self.log.debug('Received {!r}'.format(data))
        self.transport.write(data)
        self.log.debug('Sent {!r}'.format(data))

    def eof_received(self):
        self.log.debug('EOF')
        if self.transport.can_write_eof():
            self.transport.write_eof()

    def connection_lost(self, error):
        if error:
            self.log.error('ERROR: {}'.format(error))
        else:
            self.log.debug('Closing connection')
        super().connection_lost(error)

# Create the server and let the loop finish the coroutine before
# starting the real event loop.
factory = event_loop.create_server(EchoServer, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)
log.debug('Listening on {}:{}'.format(*SERVER_ADDRESS))

# Enter the event loop permanently to handle all connections.
try:
    event_loop.run_forever()
finally:
    log.debug('Server stopping')
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    log.debug('Event loop ending')
    event_loop.close()
