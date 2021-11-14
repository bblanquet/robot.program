from ActionKind import ActionKind
from car.Motor import Motor
from network.MessageHandler import MessageHandler


class MotorHandler(MessageHandler):
    def __init__(self):
        self.__motor = Motor()
        self.__messages = [ActionKind.FORWARD, ActionKind.BACKWARD, ActionKind.LEFT,ActionKind.RIGHT ]


    def handle(self, message: str):
        if message in self.__messages:
            self.__motor.do(message)