from car.Camera import Camera
from car.Picture import Picture
from network.BuzzHandler import BuzzHandler
from network.CameraHandler import CameraHandler
from network.LedHandler import LedHandler
from network.PictureHandler import PictureHandler
from network.HeadHandler import HeadHandler
from network.MotorHandler import MotorHandler
from network.Socket import Socket
from picamera.camera import PiCamera

class Robot:
    def __init__(self, url: str):
        piCam = PiCamera()
        pic = Picture(piCam)
        pic.on_capture += self.__on_capture
        cam = Camera(piCam)
        cam.on_capture += self.__on_capture
        self.socket = Socket(url,
                             [HeadHandler(), PictureHandler(pic), CameraHandler(cam),MotorHandler(), BuzzHandler(), LedHandler()])
        self.socket.run()

    def __on_capture(self, data):
        self.socket.send(data)