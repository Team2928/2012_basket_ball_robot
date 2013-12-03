import wpilib
from utils import Button

# Joysticks
leftJoy = wpilib.Joystick(2)
rightJoy = wpilib.Joystick(1)

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

    shooter_Motor = wpilib.Jaguar(4)


class Loader(object):
    loader_servo = wpilib.Servo(8)

    load_button = Button(rightJoy, 5)

    end_time = .4


tipperMotor = wpilib.Jaguar(7)
rollerMotor = wpilib.Victor(10)

# Sensors
shooterEncoder = wpilib.Encoder(1, 2, False)

topLimit = wpilib.DigitalInput(9)
bottomLimit = wpilib.DigitalInput(10)

# Button Mappings
## Right Joystick ##
tipperUpButton = Button(rightJoy, 6)
tipperDownButton = Button(rightJoy, 7)

rollerUpButton = Button(rightJoy, 11)
rollerDownButton = Button(rightJoy, 10)

# Core Functions
def CheckRestart():
    return
    # We need to do something about this at some point.....
