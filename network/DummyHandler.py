from network.MessageHandler import MessageHandler


class DummyHandler(MessageHandler):
    def handle(self, message: str):
        print(f'### received: {message}')
