import random
from math import floor
import matplotlib.pyplot as plt


def flip_coin():
    trials = [sum([random.randint(0, 1) for _ in range(10)]) for _ in range(1000)]
    frequencies = [trials.count(time) for time in range(10)]
    return {time: floor((frequencies[time]/sum(frequencies)) * 100) for time, freq in enumerate(frequencies)}


def plot_graph():
    distribution = flip_coin()
    plt.plot(distribution.keys(), distribution.values())
    plt.ylim(0, 100)
    plt.show()


if __name__ == "__main__":
    plot_graph()
