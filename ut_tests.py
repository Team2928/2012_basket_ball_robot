import unittest

import mock

import drive
import shooter
import loader


def seq(start, stop, step=1):
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    else:
        return([])


class TestDrive(unittest.TestCase):

    def setUp(self):
        self.robot_drive = mock.RobotDrive()

        self.joy = mock.JoyStick()
        self.photo_sensors = [ mock.DigitalInput() for x in range(5)]
        self.hs_button = mock.Button()
        self.align_button = mock.Button()


        class MockDriveConfig(object):
            # Motors & Drive System
            robot_drive = self.robot_drive
            drive_joy = self.joy

            photo_sensors = self.photo_sensors

            align_button = self.align_button
            hs_button = self.hs_button

        self.drive = drive.Drive(MockDriveConfig)

    def tearDown(self):
        pass

    def test_throttle(self):
        self.joy.x = 0.0

        # Sweep forward
        for y in seq(-1.0, 1.0, 0.1):
            self.joy.y = y

            self.drive.tick()

            self.assertEquals(self.robot_drive.speed, self.joy.y)
            self.assertEquals(self.robot_drive.rotation, self.joy.x)

        # Sweep back
        for y in seq(1.0, -1.0, -0.1):
            self.joy.y = y

            self.drive.tick()

            self.assertEquals(self.robot_drive.speed, self.joy.y)
            self.assertEquals(self.robot_drive.rotation, self.joy.x)

    def test_steering(self):
        self.joy.y = 0.0

        # Sweep forward
        for x in seq(-1.0, 1.0, 0.1):
            self.joy.x = x

            self.drive.tick()

            self.assertEquals(self.robot_drive.speed, self.joy.y)
            self.assertEquals(self.robot_drive.rotation, self.joy.x)

        # Sweep back
        for x in seq(1.0, -1.0, -0.1):
            self.joy.x = x

            self.drive.tick()

            self.assertEquals(self.robot_drive.speed, self.joy.y)
            self.assertEquals(self.robot_drive.rotation, self.joy.x)

    def test_half_speed_throttle(self):
        self.hs_button.pressed = True

        self.joy.x = 0.0

        # Sweep forward
        for y in seq(-1.0, 1.0, 0.1):
            self.joy.y = y

            self.drive.tick()

            self.assertEquals(self.robot_drive.speed, self.joy.y/2)
            self.assertEquals(self.robot_drive.rotation, self.joy.x)

        # Sweep back
        for y in seq(1.0, -1.0, -0.1):
            self.joy.y = y

            self.drive.tick()

            self.assertEquals(self.robot_drive.speed, self.joy.y/2)
            self.assertEquals(self.robot_drive.rotation, self.joy.x)

    def test_half_speed_steering(self):
        self.hs_button.pressed = True

        self.joy.y = 0.0

        # Sweep forward
        for x in seq(-1.0, 1.0, 0.1):
            self.joy.x = x

            self.drive.tick()

            self.assertEquals(self.robot_drive.speed, self.joy.y)
            self.assertEquals(self.robot_drive.rotation, self.joy.x/2)

        # Sweep back
        for x in seq(1.0, -1.0, -0.1):
            self.joy.x = x

            self.drive.tick()

            self.assertEquals(self.robot_drive.speed, self.joy.y)
            self.assertEquals(self.robot_drive.rotation, self.joy.x/2)


class TestShooter(unittest.TestCase):
    def setUp(self):
        self.joy = mock.JoyStick()
        self.latch_button = mock.Button()
        self.latch_servo = mock.Servo()
        self.shooter_motor = mock.Motor()

        self.shooter = shooter.Shooter(self.joy, self.latch_button,
                                    self.latch_servo, self.shooter_motor)

    def tearDown(self):
        pass

    """ It's just setting a motor in the loader module, but what the hell"""
    def test_shooter_motor(self):
        self.joy.x = 0.0

        # Sweep forward
        for y in seq(-1.0, 1.0, 0.1):
            self.joy.y = y

            self.shooter.tick(10)

            self.assertEquals(self.shooter_motor.speed, self.joy.y)
            self.assertEquals(self.shooter_motor.Get(), self.joy.y)

        # Sweep back
        for y in seq(1.0, -1.0, -0.1):
            self.joy.y = y

            self.shooter.tick(10)

            self.assertEquals(self.shooter_motor.speed, self.joy.y)
            self.assertEquals(self.shooter_motor.Get(), self.joy.y)


class TestLoader(unittest.TestCase):
    def setUp(self):
        self.load_button = mock.Button()
        self.load_servo = mock.Servo()

        self.loader = loader.Loader(self.load_button,
                                    self.load_servo)

    def tearDown(self):
        pass

    ## Add in tests



if __name__ == '__main__':
        unittest.main()
