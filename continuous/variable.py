class Variable:
    
    def __init__(self, clock, value):
        self.clock = clock
        self.value = value
        self.derivative = 0
        
    def update(self):
        self.value += self.derivative * self.clock.step
