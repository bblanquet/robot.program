from ActionKind import ActionKind
from car.Buzzer import Buzzer
from network.MessageHandler import MessageHandler

class BuzzHandler(MessageHandler):
    def __init__(self):
        self.__buzzer = Buzzer()

    def handle(self, message: str):
        if message == ActionKind.BUZZ:
            self.__buzzer.do(message)