from Clock import Clock
from Monitor import Monitor
from Graph import Graph
from Variable import Variable

class SimulationFramework:

    def __init__(self, step, duration):
        # Initialize the simulation framework here
        self.clock = Clock(step)
        self.monitor = Monitor(self.clock, duration)
        self.graph = Graph()

    def run(self):
        while self.monitor.moreTime():
            self.clock.tick()
            self.update()
        self.show()

    def update(self):
        # Update the simulation here
        pass

    def show(self):
        # Show the simulation results here
        self.graph.show()


class SimulationApp(SimulationFramework):
    def __init__(self, title, duration, mass, damping, stiffness):
        super().__init__(0.01, duration)
        self.graph.setTitle(title)
        self.mass = mass
        self.damping = damping
        self.stiffness = stiffness
        self.dxt = Variable(self.clock, 0)
        self.xt = Variable(self.clock, 0)

    def update(self):
        # Update the simulation here
        force = 0.0
        if self.clock.getTime() >= 0.5 and self.clock.getTime() <= 0.6:
            force = 10.0
        else:
            force = 0.0
        self.dxt.setDerivative(force-(self.damping/self.mass)*self.dxt.getValue()-(self.stiffness/self.mass)*self.xt.getValue())
        self.xt.setDerivative(self.dxt.getValue())
        self.dxt.update()
        self.xt.update()
        self.graph.update(self.clock.getTime(), {'F(t)x20N': force/20.0, 'x(t)': self.xt.getValue(), 'dx(t)/dt': self.dxt.getValue()})

