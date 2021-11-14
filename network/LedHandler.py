from ActionKind import ActionKind
from car.LedPicker import LedPicker
from network.MessageHandler import MessageHandler

class LedHandler(MessageHandler):
    def __init__(self):
        self.__ledPicker = LedPicker()
        self.__messages = [ActionKind.BLUE, ActionKind.RED, ActionKind.GREEN ]


    def handle(self, message: str):
        if message in self.__messages:
            self.__ledPicker.do(message)