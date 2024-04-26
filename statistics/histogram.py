import matplotlib.pyplot as plt

class Histogram:
    def __init__(self, data):
        self.data = data

    def plot(self):
        plt.hist(self.data, bins='auto')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Histogram')
        plt.grid(True)
        plt.show()
