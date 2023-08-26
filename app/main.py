from random import randint

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    attempts = 10_000

    flips = [0 for i in range(0, 11)]

    for _ in range(attempts):
        heads = sum([randint(0, 1) for _ in range(10)])
        flips[heads] += 1

    return {
        i: round(heads / attempts * 100, 2)
        for i, heads in enumerate(flips)
    }


def draw_gaussian_distribution_graph() -> None:
    flips = flip_coin()

    x_points = np.array(list(flips.keys()))
    y_points = np.array(list(flips.values()))

    plt.plot(x_points, y_points)

    plt.xticks(np.arange(0, 11))
    plt.yticks(np.arange(0, 101, 10))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
