from SimulationApp import SimulationApp

def force_callback(t):
    if t >= 0.2 and t <= 1.5:
        return 20.0
    else:
        return 0.0

if __name__ == "__main__":
    title = 'Škoda Superb Mass-Spring-Damper System'
    step = 0.01
    duration = 4.0
    mass = 1500.0
    dumping = 4*3000.0
    stiffness = 4*50000.0
    app = SimulationApp(title, step,duration, mass, dumping, stiffness, force_callback)
    app.run()