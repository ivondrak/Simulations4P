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
        fig, axs = plt.subplots(nrows=len(self.variables), sharex=True)
        fig.suptitle(self.title)

        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        for ax, (label, variable), color in zip(axs, self.variables.items(), colors):
            ax.plot(self.time, variable, label=label, color=color)
            ax.set_ylabel(label)
            ax.yaxis.label.set_color(color)
            ax.tick_params(axis='y', colors=color)
            ax.grid(True)

        axs[-1].set_xlabel('Time [s]')
        plt.show()