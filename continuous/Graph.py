import matplotlib.pyplot as plt

class Graph:

    def __init__(self, title='Graph'):
        self.variables = {}
        self.time = []
        self.title = title

    def setTitle(self, title):
        self.title = title
        
    def update(self, time, variables):
        self.time.append(time)
        for label, variable in variables.items():
            if label not in self.variables:
                self.variables[label] = []
            self.variables[label].append(variable)

    def show(self):
        for label, variable in self.variables.items():
            plt.plot(self.time, variable, label=label)

        plt.xlabel('Time')
        plt.ylabel('Variable')
        plt.title(self.title)
        plt.legend()
        plt.show()