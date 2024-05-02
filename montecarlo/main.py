import sys
sys.path.append('.')

from simulation_app import SimulationApp

if __name__ == "__main__":
    title = "Inaccuracy of the Robot in [mm]"
    number_of_samples = 1000
    app = SimulationApp(title, number_of_samples)
    app.run()