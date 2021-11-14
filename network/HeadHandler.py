from ActionKind import ActionKind
from car.Head import Head
from network.MessageHandler import MessageHandler


class HeadHandler(MessageHandler):
    def __init__(self):
        self.__head = Head()
        self.__messages = [ActionKind.HEAD_UP, ActionKind.HEAD_DOWN, ActionKind.HEAD_LEFT,ActionKind.HEAD_RIGHT,ActionKind.HEAD_CENTER ]

    def handle(self, message: str):
        if message in self.__messages:
            self.__head.do(message)
