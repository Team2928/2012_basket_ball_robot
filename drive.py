import wpilib
from config import *

__all__ = ['Drive']

class Drive:
    def __init__(self, driveJoy, halfspeedButton, alignButton ):
        self.halfSpeed = True
        self.speed = 0
        self.rot = 0

        self.aligning = False

        self.left = 0
        self.right = 0

        self.driveJoy = driveJoy
        self.hsButton = halfspeedButton
        self.alignButton = alignButton

    def tick(self):
        if self.alignButton.get():
            self.align()
        else:
            self.speed = self.driveJoy.GetY()
            self.rot = self.driveJoy.GetX()
            if self.hsButton.get():
                self.speed /= 2
                self.rot /= 2
            robotDrive.ArcadeDrive(self.speed, self.rot)

    def align(self):
        if photo1.Get():
            self.left += .25
        if photo2.Get():
            self.left -= .25
        if photo3.Get():
            self.right += .25
        if photo4.Get():
            self.right -= .25
        #if self.left == 0 and self.right == 0:
        #    self.aligning = False

        leftMotor.Set(self.left)
        rightMotor.Set(self.right)
