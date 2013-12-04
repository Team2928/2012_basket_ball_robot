import wpilib
from utils import Button

# Joysticks
leftJoy = wpilib.Joystick(1)
rightJoy = wpilib.Joystick(2)

leftMotor = wpilib.Jaguar(1)
rightMotor = wpilib.Jaguar(2)


class Drive(object):
    robot_drive = wpilib.RobotDrive(leftMotor, rightMotor)

    drive_joy = leftJoy

    photo_sensors = [ wpilib.DigitalInput(x+4) for x in range(5) ]

    # Buttons
    align_button = Button(rightJoy, 3)
    hs_button = Button(leftJoy, 1)


class Shooter(object):
    joystick = rightJoy

    latch_button = Button(rightJoy, 4)

    latch_servo = wpilib.Servo(5)

    shooter_motor = wpilib.Jaguar(4)


class Loader(object):
    loader_servo = wpilib.Servo(8)

    load_button = Button(rightJoy, 5)

    end_time = .4


class Tipper(object):
    motor = wpilib.Jaguar(7)

    up_button = Button(rightJoy, 6)
    down_button = Button(rightJoy, 7)


class Roller(object):
    motor = wpilib.Victor(10)

    up_button = Button(rightJoy, 11)
    down_button= Button(rightJoy, 10)


# Sensors
shooterEncoder = wpilib.Encoder(1, 2, False)

topLimit = wpilib.DigitalInput(9)
bottomLimit = wpilib.DigitalInput(10)

# Core Functions
def CheckRestart():
    return
    # We need to do something about this at some point.....
