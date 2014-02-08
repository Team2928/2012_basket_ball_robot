import common


__all__ = ['Drive']


class Drive(common.ComponentBase):

    def __init__(self, config):
        self.left = 0
        self.right = 0

        self.robot_drive = config.robot_drive
        self.drive_joy = config.drive_joy
        self.hs_button = config.hs_button
        self.align_button = config.align_button

        self.photo_sensors = config.photo_sensors

    def op_init(self):
        self.robot_drive.StopMotor()

    def op_tick(self, time):
        if self.align_button.get():
            self.align()
        else:
            speed = self.drive_joy.GetY()
            rot = self.drive_joy.GetX()
            if self.hs_button.get():
                speed /= 2
                rot /= 2
            self.robot_drive.ArcadeDrive(speed, rot)

    def align(self):

        motorSpeed = .25

        if self.frontLeft and self.backLeft:
            self.left = 0
        elif not self.frontLeft and self.backLeft
            self.left = -motorSpeed
        else:
            self.left = motorSpeed


        if self.frontRight and self.backRight:
            self.right = 0
        elif not self.frontRight and self.backRight
            self.right = -motorSpeed
        else:
            self.right = motorSpeed 
            
            
        # I think this should work....?
        self.robot_drive.SetLeftRightMotorOutputs(self.left, self.right)
