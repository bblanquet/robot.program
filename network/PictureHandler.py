from ActionKind import ActionKind
from car.Picture import Picture
from network.MessageHandler import MessageHandler


class PictureHandler(MessageHandler):
    def __init__(self, cam: Picture):
        self.__picture = cam

    def handle(self, message: str):
        if message == ActionKind.CAPTURE:
            self.__picture.do(message)