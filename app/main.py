import random
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict


def flip_coin() -> dict:
    results = defaultdict(lambda: 0)
    for _ in range(0, 10000):
        flips = sum([random.randint(0, 1) for _ in range(10)])
        results[flips] += (1 / 100)
    return results


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    xpoints = np.array([key for key in data.keys()])
    ypoints = np.array([value for value in data.values()])

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
