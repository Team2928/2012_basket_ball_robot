import wpilib
from config import *

__all__ = ['Shooter']

class Shooter:
    def __init__(self):
        self.timer = wpilib.Timer()
        self.endTime = .3

        self.timer.Start()

        self.shooting = False

    def unlatch(self):
        if not(self.shooting):
            latchServo.Set(.4)
            self.timer.Reset()
            self.shooting = True

    def tick(self):
        if self.shooting:
            if self.timer.Get() >= self.endTime:
                latchServo.Set(.9)
                self.shooting = False

    def setDelay(self):
        self.endTime = rightJoy.GetZ()
