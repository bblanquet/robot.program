import time
from ActionKind import ActionKind
from car.Doer import Doer

from car.PCA9685 import PCA9685

class Motor(Doer):
    def __init__(self):
        super(Motor, self).__init__()
        self.pwm = PCA9685(0x40, debug=True)
        self.pwm.setPWMFreq(50)

    def __duty_range(self, duty1, duty2, duty3, duty4):
        if duty1 > 4095:
            duty1 = 4095
        elif duty1 < -4095:
            duty1 = -4095

        if duty2 > 4095:
            duty2 = 4095
        elif duty2 < -4095:
            duty2 = -4095

        if duty3 > 4095:
            duty3 = 4095
        elif duty3 < -4095:
            duty3 = -4095

        if duty4 > 4095:
            duty4 = 4095
        elif duty4 < -4095:
            duty4 = -4095
        return duty1, duty2, duty3, duty4

    def __left_Upper_Wheel(self, duty):
        if duty > 0:
            self.pwm.setMotorPwm(0, 0)
            self.pwm.setMotorPwm(1, duty)
        elif duty < 0:
            self.pwm.setMotorPwm(1, 0)
            self.pwm.setMotorPwm(0, abs(duty))
        else:
            self.pwm.setMotorPwm(0, 4095)
            self.pwm.setMotorPwm(1, 4095)

    def __left_Lower_Wheel(self, duty):
        if duty > 0:
            self.pwm.setMotorPwm(3, 0)
            self.pwm.setMotorPwm(2, duty)
        elif duty < 0:
            self.pwm.setMotorPwm(2, 0)
            self.pwm.setMotorPwm(3, abs(duty))
        else:
            self.pwm.setMotorPwm(2, 4095)
            self.pwm.setMotorPwm(3, 4095)

    def __right_Upper_Wheel(self, duty):
        if duty > 0:
            self.pwm.setMotorPwm(6, 0)
            self.pwm.setMotorPwm(7, duty)
        elif duty < 0:
            self.pwm.setMotorPwm(7, 0)
            self.pwm.setMotorPwm(6, abs(duty))
        else:
            self.pwm.setMotorPwm(6, 4095)
            self.pwm.setMotorPwm(7, 4095)

    def __right_Lower_Wheel(self, duty):
        if duty > 0:
            self.pwm.setMotorPwm(4, 0)
            self.pwm.setMotorPwm(5, duty)
        elif duty < 0:
            self.pwm.setMotorPwm(5, 0)
            self.pwm.setMotorPwm(4, abs(duty))
        else:
            self.pwm.setMotorPwm(4, 4095)
            self.pwm.setMotorPwm(5, 4095)

    def __setMotorModel(self, duty1, duty2, duty3, duty4):
        duty1, duty2, duty3, duty4 = self.__duty_range(duty1, duty2, duty3, duty4)
        self.__left_Upper_Wheel(duty1)
        self.__left_Lower_Wheel(duty2)
        self.__right_Upper_Wheel(duty3)
        self.__right_Lower_Wheel(duty4)

    def _execute(self, action: ActionKind):
        if action == ActionKind.FORWARD:
            self.__forward()
        elif action == ActionKind.BACKWARD:
            self.__backward()
        elif action == ActionKind.RIGHT:
            self.__right()
        elif action == ActionKind.LEFT:
            self.__left()

    def __backward(self):
        self.__setMotorModel(1000, 1000, 1000, 1000)
        time.sleep(1)
        self.__setMotorModel(0, 0, 0, 0)

    def __forward(self):
        self.__setMotorModel(-1000, -1000, -1000, -1000)
        time.sleep(1)
        self.__setMotorModel(0, 0, 0, 0)

    def __left(self):
        self.__setMotorModel(-1000, -1000, 4000, 4000)
        time.sleep(1)
        self.__setMotorModel(0, 0, 0, 0)

    def __right(self):
        self.__setMotorModel(4000, 4000, -1000, -1000)
        time.sleep(1)
        self.__setMotorModel(0, 0, 0, 0)

