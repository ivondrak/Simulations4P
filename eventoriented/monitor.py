from events import Agenda

class Monitor:
    def __init__(self, clock, number_of_samples):
        self.clock = clock
        self.agenda = Agenda(self.clock)
        self.number_of_samples = number_of_samples
        self.samples_taken = 0

    def moreEvents(self):
        if self.agenda.isEmpty():
            return False
        else:
            return True
        
    def moreSamples(self):
        if self.samples_taken < self.number_of_samples:
            return True
        else:
            return False
        
    def update(self):
        self.samples_taken += 1

    def show(self):
        print("Number of samples taken: ", self.samples_taken)