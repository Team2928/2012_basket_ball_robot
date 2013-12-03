import common


__all__ = ['Loader']


class Loader(common.ComponentBase):

    def __init__(self, config):
        self.load_button = config.load_button
        self.loader_servo = config.loader_servo

        self.end_time = config.end_time

        self.elapsed = 0
        self.pTime = 0

        self.loading = False

    def load(self):
        if not(self.loading):
            self.loader_servo.Set(0)
            self.elapsed = 0
            self.loading = True

    def op_tick(self, time):
        self.elapsed += time - self.pTime
        self.pTime = time
        if self.load_button.get():
            self.load()
        if self.loading:
            if self.elapsed >= self.end_time:
                self.loader_servo.Set(1)
                self.loading = False
