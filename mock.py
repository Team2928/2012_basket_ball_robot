

class Button(object):

    def __init__(self):
        self.pressed = False

    def get(self):
        return self.pressed


class JoyStick(object):

    def __init__(self):
        self.x = 0
        self.y = 0

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y


class PhotoSensor(object):

    def __init__(self):
        self.state = False

    def Get(self):
        return self.state


class RobotDrive(object):

    def __init__(self):
        self.speed = 0
        self.rotation = 0

    def ArcadeDrive(self, speed, rotation):
        self.speed = speed
        self.rotation = rotation

    def StopMotor(self):
        self.speed = 0
        self.rotation = 0
