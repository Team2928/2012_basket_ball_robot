import wpilib
from utils import Button

# Joysticks
leftJoy = wpilib.Joystick(2)
rightJoy = wpilib.Joystick(1)

# Motors & Drive System
leftMotor = wpilib.Jaguar(1)
rightMotor = wpilib.Jaguar(2)
robotDrive = wpilib.RobotDrive(leftMotor, rightMotor)

shooterMotor = wpilib.Jaguar(4)
tipperMotor = wpilib.Jaguar(7)
rollerMotor = wpilib.Victor(10)

# Servos
latchServo = wpilib.Servo(5)
feederServo = wpilib.Servo(8)

# Sensors
shooterEncoder = wpilib.Encoder(1, 2, False)

photo1 = wpilib.DigitalInput(4)
photo2 = wpilib.DigitalInput(5)
photo3 = wpilib.DigitalInput(6)
photo4 = wpilib.DigitalInput(7)

topLimit = wpilib.DigitalInput(9)
bottomLimit = wpilib.DigitalInput(10)

timer = wpilib.Timer()

# Button Mappings
## Right Joystick ##
tipperUp = 6
tipperUpButton = Button(rightJoy, 6)
tipperDown = 7
tipperDownButton = Button(rightJoy, 7)

alignButtonNum = 3
alignButton = Button(rightJoy, 3)

latchButton = 4
feederButton = 5
rollerUpButton = 11
rollerDownButton = 10

## Left Joystick ##
halfSpeed = 1
hsButton = Button(leftJoy, 1)

# Core Functions
def CheckRestart():
    return
##    if leftJoy.GetRawButton(10):
##        raise SystemExit
