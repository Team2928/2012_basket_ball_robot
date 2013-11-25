
__all__ = ['Drive']

class Drive:

    def __init__(self, robot_drive, drive_joy, photo_sensors, half_speed_button,
                 align_button ):
        self.left = 0
        self.right = 0

        self.robot_drive = robot_drive
        self.drive_joy = drive_joy
        self.hs_button = half_speed_button
        self.align_button = align_button

        self.photo_sensors = photo_sensors

    def tick(self):
        if self.align_button.get():
            self.align()
        else:
            speed = self.drive_joy.GetY()
            rot = self.drive_joy.GetX()
            if self.hs_button.get():
                speed /= 2
                rot /= 2
            self.robot_drive.ArcadeDrive(speed, rot)

    def stop(self):
        self.robot_drive.StopMotor()

    def align(self):
        if self.photo_sensors[0].Get():
            self.left += .25
        if self.photo_sensors[1].Get():
            self.left -= .25
        if self.photo_sensors[2].Get():
            self.right += .25
        if self.photo_sensors[3].Get():
            self.right -= .25

        leftMotor.Set(self.left)
        rightMotor.Set(self.right)
