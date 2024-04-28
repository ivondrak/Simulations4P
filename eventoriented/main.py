import sys
sys.path.append('.')

from simulation_app import SimulationApp, GeneratorFactory
from utilities.generator import ExponentialGenerator

class ExponentialFactory(GeneratorFactory):
    
    def createArrivals(self):
        return ExponentialGenerator(1.0, self.number_of_samples, self.seed)
    
    def createServices(self):
        return ExponentialGenerator(0.5, self.number_of_samples, self.seed)

if __name__ == "__main__":
    title = 'Single queue single service simulation'
    number_of_samples = 1000
    app = SimulationApp(title, ExponentialFactory(number_of_samples, 1959))
    app.run()