class Transaction:
    def __init__(self, clock):
        self.clock = clock
        self.birth_time = clock.time
        self.next_in_line = None

    def flowTime(self):
        return self.clock.time - self.birth_time

