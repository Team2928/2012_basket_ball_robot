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

photoSensors = []
for i in range(5):
	photoSensors.append( wpilib.DigitalInput(i+4) )

topLimit = wpilib.DigitalInput(9)
bottomLimit = wpilib.DigitalInput(10)

# Button Mappings
## Right Joystick ##
tipperUpButton = Button(rightJoy, 6)
tipperDownButton = Button(rightJoy, 7)

alignButton = Button(rightJoy, 3)

latchButton = Button(rightJoy, 4)
feederButton = Button(rightJoy, 5)
rollerUpButton = Button(rightJoy, 11)
rollerDownButton = Button(rightJoy, 10)


## Left Joystick ##
hsButton = Button(leftJoy, 1)

# Core Functions
def CheckRestart():
    return
    # We need to do something about this at some point.....
