import random
import matplotlib.pyplot as plt
import numpy as np
from math import floor


def flip_coin(cases):
    dictionary = {}

    for _ in range(cases):
        heads = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                heads += 1
        dictionary[heads] = dictionary.get(heads, 0) + 1

    for key, value in dictionary.items():
        dictionary[key] = floor(value / cases * 100)

    return dict(sorted(dictionary.items()))


def draw_gaussian_distribution_graph():

    data = flip_coin(1000)

    heads_count = [*data.keys()]
    percentage = [*data.values()]

    plt.ylim(0, 100)
    x_points = np.array(heads_count)
    y_points = np.array(percentage)

    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 101, 10))

    plt.plot(x_points, y_points)

    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.title("Gaussian distribution")

    plt.show()
