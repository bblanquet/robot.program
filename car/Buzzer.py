import time
import RPi.GPIO as GPIO
from ActionKind import ActionKind
from car.Doer import Doer

GPIO.setwarnings(False)
Buzzer_Pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(Buzzer_Pin,GPIO.OUT)

class Buzzer(Doer):
    def _execute(self, action:ActionKind):
        self.__buzz('1')
        time.sleep(0.5)
        self.__buzz('0')
    
    def __buzz(self,command):
        if command!="0":
            GPIO.output(Buzzer_Pin,True)
        else:
            GPIO.output(Buzzer_Pin,False)