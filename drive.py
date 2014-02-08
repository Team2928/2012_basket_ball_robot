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
        frontLeft = self.photo_sensors[0].Get()
        backLeft = self.photo_sensors[1].Get()
        frontRight = self.photo_sensors[2].Get()
        backRight = self.photo_sensors[3].Get()
        if self.photo_sensors[0].Get():
            self.left += .25
        if self.photo_sensors[1].Get():
            self.left -= .25
        if self.photo_sensors[2].Get():
            self.right += .25
        if self.photo_sensors[3].Get():
            self.right -= .25

        # I think this should work....?
        self.robot_drive.SetLeftRightMotorOutputs(self.left, self.right)
