class Clock:

    def __init__(self, step):
        self.step = step
        self.time = 0

    def tick(self):
        self.time += self.step
