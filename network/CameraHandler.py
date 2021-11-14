from ActionKind import ActionKind
from car.Camera import Camera
from network.MessageHandler import MessageHandler


class CameraHandler(MessageHandler):
    def __init__(self, cam: Camera):
        self.__camera = cam

    def handle(self, message: str):
        if message == ActionKind.STREAM_ON:
            self.__camera.do(message)
        elif message == ActionKind.STREAM_OFF:
            self.__camera.stop()