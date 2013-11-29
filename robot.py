import wpilib

import config

from drive import Drive
from loader import Loader
from shooter import Shooter
from config import *


class MyRobot(wpilib.SimpleRobot):
    def __init__(self):
        super().__init__()
        self.loader = Loader(feederButton, feederServo)
        self.shooter = Shooter(config.Shooter)
        self.drive = Drive(config.Drive)

        self.componets = [ self.loader, self.shooter, self.drive ]

    def RobotInit(self):
        wpilib.Wait(0.25)
        shooterEncoder.Start()

    def Disabled(self):
        while wpilib.IsDisabled():
            CheckRestart()
            wpilib.Wait(0.01)

    def Autonomous(self):
        while wpilib.IsAutonomous() and wpilib.IsEnabled():
            CheckRestart()
            wpilib.Wait(0.01)

    def OperatorControl(self):
        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)

        self.drive.stop()
        shooterMotor.Set(0)
        tipperMotor.Set(0)
        rollerMotor.Set(0)

        while self.IsOperatorControl() and self.IsEnabled():
            dog.Feed()
            CheckRestart()
            for componet in self.componets:
                componet.tick(wpilib.Timer.GetFPGATimestamp())

            ## Tipper Up and Down
            if tipperUpButton.get():
                tipperMotor.Set(-1)
            elif tipperDownButton.get():
                tipperMotor.Set(1)
            else:
                tipperMotor.Set(0)

            ## Roller Up and Down
            if rollerUpButton.get():
                rollerMotor.Set(-1)
            elif rollerDownButton.get()):
                rollerMotor.Set(1)
            else:
                rollerMotor.Set(0)

            ## Debug & Tuning

            wpilib.Wait(0.01)

def run():
    robot = MyRobot()
    robot.StartCompetition()
