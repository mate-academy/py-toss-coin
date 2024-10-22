from random import randint

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict[int: float]:
    flip_times = dict.fromkeys(range(0, 11), 0)

    for _ in range(10000):
        temp = 0
        for _ in range(10):
            if randint(0, 1):
                temp += 1
        flip_times[temp] += 1

    return {
        key: value / 100
        for key, value in flip_times.items()
    }


def draw_gaussian_distribution_graph() -> None:
    flip_results = flip_coin()

    x_points = np.array(list(flip_results.keys()))
    y_points = np.array(list(flip_results.values()))

    plt.plot(x_points, y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xticks(x_points)
    plt.ylim(0, 100)
    plt.yticks(np.arange(0, 101, 10))

    plt.show()
