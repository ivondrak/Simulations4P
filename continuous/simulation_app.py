from clock import Clock
from monitor import Monitor
from graph import Graph
from variable import Variable

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
    def __init__(self, title, step, duration, mass, damping, stiffness, force_callback):
        super().__init__(step, duration)
        self.graph.setTitle(title)
        self.mass = mass
        self.damping = damping
        self.stiffness = stiffness
        self.dxt = Variable(self.clock, 0)
        self.xt = Variable(self.clock, 0)
        self.force_callback = force_callback

    def update(self):
        # Update the simulation here
        force = self.force_callback(self.clock.time)
        self.dxt.derivative = force-(self.damping/self.mass)*self.dxt.value-(self.stiffness/self.mass)*self.xt.value
        self.xt.derivative = self.dxt.value
        self.dxt.update()
        self.xt.update()
        self.graph.update(self.clock.time, {'F(t) [N]': force, 'x(t) [m]': self.xt.value, 'v(t) [m/s]': self.dxt.value})

