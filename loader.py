import wpilib
from config import *

__all__ = ['Loader']

class Loader:
    def __init__(self):
        self.timer = wpilib.Timer()
        self.endTime = .4

        self.timer.Start()

        self.loading = False

    def load(self):
        if not(self.loading):
            feederServo.Set(0)
            self.timer.reset()
            self.loading = True

    def tick(self):
        if self.loading:
            if self.timer.Get() >= self.endTime:
                feederServo.Set(1)
                self.loading = False

    def setDelay(self):
        self.endTime = rightJoy.GetZ() * 2
