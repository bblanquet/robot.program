from ActionKind import ActionKind
from car.Doer import Doer
from car.Led import Led

class LedPicker(Doer):
    def __init__(self):
        super(LedPicker, self).__init__()
        self.led=Led()
    
    def _execute(self, action: ActionKind):
        if action == ActionKind.BLUE:
            self.led.colorWipe(self.led.strip, self.Color(0, 0, 255),100)  # Blue wipe
            self.led.colorWipe(self.led.strip, self.Color(0,0,0),10)
        elif action == ActionKind.RED:
            self.led.colorWipe(self.led.strip, self.Color(255,0, 0),100)  # Red wipe
            self.led.colorWipe(self.led.strip, self.Color(0,0,0),10)
        elif action == ActionKind.GREEN:
            self.led.colorWipe(self.led.strip, self.Color(0, 255, 0),100)  # Green wipe
            self.led.colorWipe(self.led.strip, self.Color(0,0,0),10)

            
    def Color(self, red, green, blue, white=0):
        """Convert the provided red, green, blue color to a 24-bit color value.
        Each color component should be a value 0-255 where 0 is the lowest intensity
        and 255 is the highest intensity.
        """
        return (white << 24) | (red << 16) | (green << 8) | blue