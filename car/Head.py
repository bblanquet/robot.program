import time
from ActionKind import ActionKind
from car.Doer import Doer

from car.PCA9685 import PCA9685


class Head(Doer):
    def __init__(self):
        super(Head, self).__init__()
        self.PwmServo = PCA9685(0x40, debug=True)
        self.PwmServo.setPWMFreq(50)
        self.PwmServo.setServoPulse(8, 1500)
        self.PwmServo.setServoPulse(9, 1500)

    def __setServoPwm(self, channel, angle, error=10):
        angle = int(angle)
        if channel == '0':
            self.PwmServo.setServoPulse(8, 2500 - int((angle + error) / 0.09))
        elif channel == '1':
            self.PwmServo.setServoPulse(9, 500 + int((angle + error) / 0.09))
        elif channel == '2':
            self.PwmServo.setServoPulse(10, 500 + int((angle + error) / 0.09))
        elif channel == '3':
            self.PwmServo.setServoPulse(11, 500 + int((angle + error) / 0.09))
        elif channel == '4':
            self.PwmServo.setServoPulse(12, 500 + int((angle + error) / 0.09))
        elif channel == '5':
            self.PwmServo.setServoPulse(13, 500 + int((angle + error) / 0.09))
        elif channel == '6':
            self.PwmServo.setServoPulse(14, 500 + int((angle + error) / 0.09))
        elif channel == '7':
            self.PwmServo.setServoPulse(15, 500 + int((angle + error) / 0.09))

    def _execute(self, action: ActionKind):
        if action == ActionKind.HEAD_CENTER:
            self.__center()
        elif action == ActionKind.HEAD_LEFT:
            self.__left()
        elif action == ActionKind.HEAD_RIGHT:
            self.__right()
        elif action == ActionKind.HEAD_DOWN:
            self.__down()
        elif action == ActionKind.HEAD_UP:
            self.__up()
        elif action == ActionKind.HEAD_RIGHT:
            self.__right()
    
    def __left(self):
        self.__setServoPwm('0', 0)

    def __right(self):
        self.__setServoPwm('0', 90)

    def __up(self):
        self.__setServoPwm('1', 60)

    def __center(self):
        self.__setServoPwm('0', 45)
        self.__setServoPwm('1', 45)

    def __down(self):
        self.__setServoPwm('1', 30)
