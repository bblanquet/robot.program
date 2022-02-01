
from picamera.camera import PiCamera
from ActionKind import ActionKind
from car.Doer import Doer
from tool.EventHandler import EventHandler
import base64
from io import BytesIO

class Camera(Doer):
    def __init__(self, cam: PiCamera):
        super(Camera,self).__init__()
        self.camera = cam
        self.on_capture = EventHandler()
        self.buffer = BytesIO()
        
    def stop(self):
        self._is_busy = False
    
    def _execute(self, action:ActionKind):
        for _ in self.camera.capture_continuous(self.buffer,use_video_port=True, format='jpeg'):
            if not self._is_busy:
                break
            self.buffer.seek(0)
            base64_output = base64.b64encode(self.buffer.getvalue())
            self.on_capture.fire(base64_output)
            self.buffer.flush()