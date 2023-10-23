import random
from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    distribution = defaultdict(int)

    for _ in range(0, 10000):
        flips = sum([random.randint(0, 1) for _ in range(10)])
        distribution[flips] += (1 / 100)

    return distribution


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    x_axis = np.arange(distribution.keys())
    y_axis = np.arange(distribution.values())

    plt.plot(x_axis, y_axis)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
