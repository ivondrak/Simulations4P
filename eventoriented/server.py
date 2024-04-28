class Server:
    def __init__(self, clock):
        self.clock = clock
        self.available = True
        self.start_time = self.clock.time
        self.time_of_last_change = 0
        self.use_integral = 0

    def isAvailable(self):
        return self.available

    def seize(self):
        if self.available:
            self.available = False
            self.time_of_last_change = self.clock.time
        else:
            print('Server is busy')
        self.available = False

    def release(self):
        if not self.available:
            self.available = True
            self.use_integral += self.clock.time - self.time_of_last_change
            self.time_of_last_change = self.clock.time
        else:
            print('Server is available')
        self.available = True

    def utilization(self):
        if self.clock.time > 0:
            return self.use_integral / (self.clock.time - self.start_time)
        else:
            return 0

    def show(self):
        print('Server utiliation: ', round(self.utilization(), 2))