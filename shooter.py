import common


__all__ = ['Shooter']


class Shooter(common.ComponentBase):

    def __init__(self, config):
        self.joystick = config.joystick
        self.latch_button = config.latch_button
        self.latch_servo = config.latch_servo
        self.shooter_motor = config.shooter_motor

        self.elapsed = 0
        self.endTime = .3
        self.pTime = 0

        self.shooting = False

    def unlatch(self):
        if not(self.shooting):
            self.latch_servo.Set(.4)
            self.elapsed = 0
            self.shooting = True

    def op_init(self):
        self.shooter_motor.Set(0)

    def op_tick(self, time):
        self.elapsed += time - self.pTime
        self.pTime = time

        self.shooter_motor.Set(self.joystick.GetY())

        if self.latch_button.get():
            self.unlatch()
        if self.shooting:
            if self.elapsed >= self.endTime:
                self.latch_servo.Set(.9)
                self.shooting = False
