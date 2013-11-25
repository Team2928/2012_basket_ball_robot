
__all__ = ['Shooter']

class Shooter:
    def __init__(self, joy, latchButton, latchServo, shooterMotor):
        self.joy = joy
        self.latch_button = latchButton
        self.latch_servo = latchServo
        self.shooter_motor = shooterMotor

        self.elapsed = 0
        self.endTime = .3
        self.pTime = 0

        self.shooting = False

    def unlatch(self):
        if not(self.shooting):
            self.latch_servo.Set(.4)
            self.elapsed = 0
            self.shooting = True

    def tick(self, time):
        self.elapsed += time - self.pTime
        self.pTime = time

        self.shooter_motor.Set(self.joy.GetY())

        if latch_button.get():
            self.unlatch()
        if self.shooting:
            if self.elapsed >= self.endTime:
                self.latch_servo.Set(.9)
                self.shooting = False
