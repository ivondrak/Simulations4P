class Monitor:
    def __init__(self, number_of_samples=1000):
        self.number_of_samples = number_of_samples

    def anotherSample(self):
        self.number_of_samples -= 1
        return self.number_of_samples >= 0