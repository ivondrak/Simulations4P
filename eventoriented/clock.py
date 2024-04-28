class Clock:

    def __init__(self, time=0):
        self.time = time
        self.time_of_next_event = float('inf')

    def show(self):
        print("Clock time is: ", round(self.time, 2))
