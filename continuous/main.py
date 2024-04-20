from SimulationApp import SimulationApp

if __name__ == "__main__":
    title = 'Škoda Superb Mass-Spring-Damper System'
    duration = 3.0
    mass = 1500.0
    dumping = 4*3000.0
    stiffness = 4*50000.0
    app = SimulationApp(title, duration, mass, dumping, stiffness)
    app.run()