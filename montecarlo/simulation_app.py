from monitor import Monitor
from utilities.generator import UniformGenerator, NormalGenerator
from utilities.histogram import Histogram
import math

class SimulationFramework:

    def __init__(self, number_of_samples=1000, seed=None):
        self.samples = []
        self.monitor = Monitor(number_of_samples)

    def run(self):
        while self.monitor.anotherSample():
            sample = self.run_sample()
            self.samples.append(sample)
        self.show()

    def run_sample(self):
        pass

    def show(self):
        pass


class SimulationApp(SimulationFramework):

    def __init__(self, title, number_of_samples, seed=None):
        super().__init__(number_of_samples, seed)
        pi = 3.14159265359
        self.title = title
        self.coord_f = UniformGenerator(0, 3*pi/2, number_of_samples, seed)
        self.coord_z = UniformGenerator(1, 1.6, number_of_samples, seed)
        self.coord_y = UniformGenerator(0.5, 1, number_of_samples, seed)
        self.in_acc_f = NormalGenerator(0, pi/500, number_of_samples, seed)
        self.in_acc_z = NormalGenerator(0, 0.005, number_of_samples, seed)
        self.in_acc_y = NormalGenerator(0, 0.002, number_of_samples, seed)
        self.coord_f.generate()
        self.coord_z.generate()
        self.coord_y.generate()
        self.in_acc_f.generate()
        self.in_acc_z.generate()
        self.in_acc_y.generate()


    def run_sample(self):
        f = self.coord_f.next()
        z = self.coord_z.next()
        y = self.coord_y.next()
        df = self.in_acc_f.next()
        dz = self.in_acc_z.next()
        dy = self.in_acc_y.next()

        #absolute coordinates
        x0 = -math.sin(f) * y
        y0 = math.cos(f) * y
        z0 = z
        abs_x = -math.sin(f + df) * (y + dy)
        abs_y = math.cos(f + df) * (y + dy)
        abs_z = z + dz

        sample = math.sqrt((x0 - abs_x)**2 + (y0 - abs_y)**2 + (z0 - abs_z)**2)*1000
        return sample
    

    def show(self):
        print(self.title)
        print('Mean distance: ', sum(self.samples) / len(self.samples))
        Histogram(self.samples, self.title, "Distance [mm]", "Frequency").plot()