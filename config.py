import wpilib
from utils import Button

# Joysticks
leftJoy = wpilib.Joystick(2)
rightJoy = wpilib.Joystick(1)

leftMotor = wpilib.Jaguar(1)
rightMotor = wpilib.Jaguar(2)


class Drive(object):
    # Motors & Drive System
    robot_drive = wpilib.RobotDrive(leftMotor, rightMotor)
    drive_joy = leftJoy

    photo_sensors = [ wpilib.DigitalInput(x+4) for x in range(5) ]

    align_button = Button(rightJoy, 3)
    hs_button = Button(leftJoy, 1)


shooterMotor = wpilib.Jaguar(4)
tipperMotor = wpilib.Jaguar(7)
rollerMotor = wpilib.Victor(10)

# Servos
feederServo = wpilib.Servo(8)
latchServo = wpilib.Servo(5)

# Sensors
shooterEncoder = wpilib.Encoder(1, 2, False)


topLimit = wpilib.DigitalInput(9)
bottomLimit = wpilib.DigitalInput(10)

# Button Mappings
## Right Joystick ##
tipperUpButton = Button(rightJoy, 6)
tipperDownButton = Button(rightJoy, 7)

latchButton = Button(rightJoy, 4)

feederButton = Button(rightJoy, 5)
rollerUpButton = Button(rightJoy, 11)
rollerDownButton = Button(rightJoy, 10)

# Core Functions
def CheckRestart():
    return
    # We need to do something about this at some point.....
