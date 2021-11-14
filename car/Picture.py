import base64
from picamera import PiCamera
from ActionKind import ActionKind
from car.Doer import Doer
from tool.EventHandler import EventHandler
from io import BytesIO


class Picture(Doer):
    def __init__(self, cam: PiCamera):
        super(Picture, self).__init__()
        self.camera = cam
        self.on_capture = EventHandler()

    def _execute(self, action: ActionKind):
        output = BytesIO()
        self.camera.capture(output, format='jpeg')
        output.seek(0)
        base64_output = base64.b64encode(output.getvalue())
        self.on_capture.fire(base64_output)
