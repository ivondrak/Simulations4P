class Monitor:

    def __init__(self, clock, duration):
        self.clock = clock
        self.duration = duration

    def moreTime(self):
        return self.clock.time <= self.duration

