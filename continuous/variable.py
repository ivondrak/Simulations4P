class Variable:
    
    def __init__(self, clock, value):
        self.clock = clock
        self.value = value

    def setDerivative(self, derivative):
        self.derivative = derivative

    def getValue(self):
        return self.value
        
    def update(self):
        self.value += self.derivative * self.clock.getStep()
