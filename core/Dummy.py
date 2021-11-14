from network.DummyHandler import DummyHandler
from network.Socket import Socket


class Dummy:
    def __init__(self):
        self.socket = Socket("ws://localhost:49156/ws", [DummyHandler()])
        self.socket.run()
