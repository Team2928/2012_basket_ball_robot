import wpilib

import config
import common

from drive import Drive
from loader import Loader
from shooter import Shooter


class MyRobot(wpilib.SimpleRobot):
    def __init__(self):
        super().__init__()

        self.components = []

        self.loader = Loader(config.Loader)
        self.components.append(self.loader)

        self.shooter = Shooter(config.Shooter)
        self.components.append(self.shooter)

        self.drive = Drive(config.Drive)
        self.components.append(self.drive)

        self.tipper = common.ButtonControlledMotor(config.Tipper)
        self.components.append(self.tipper)

        self.roller = common.ButtonControlledMotor(config.Roller)
        self.components.append(self.roller)


    def RobotInit(self):
        wpilib.Wait(0.25)

        for component in self.components:
            component.robot_init()

    def Disabled(self):
        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)

        for componet in self.components:
            componet.disabled_init()

        while wpilib.IsDisabled():
            dog.Feed()
            CheckRestart()

            for componet in self.components:
                componet.disabled_tick(wpilib.Timer.GetFPGATimestamp())

            wpilib.Wait(0.01)

    def Autonomous(self):
        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)

        for componet in self.components:
            componet.auto_init()

        while wpilib.IsAutonomous() and wpilib.IsEnabled():
            dog.Feed()
            CheckRestart()

            for componet in self.components:
                componet.auto_tick(wpilib.Timer.GetFPGATimestamp())

            wpilib.Wait(0.01)

    def OperatorControl(self):
        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)

        for componet in self.components:
            componet.op_init()

        while self.IsOperatorControl() and self.IsEnabled():
            dog.Feed()
            CheckRestart()
            for componet in self.components:
                componet.op_tick(wpilib.Timer.GetFPGATimestamp())

            ## Debug & Tuning
            # ??
            wpilib.Wait(0.01)


def run():
    robot = MyRobot()
    robot.StartCompetition()
