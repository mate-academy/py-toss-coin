import random
from matplotlib import pyplot as plt
import numpy as np


def flip_coin(trials: int = 10000, flips: int = 10) -> dict:
    results = {}

    for i in range(trials):
        heads_count = sum(1 for i in range(flips) if random.random() < 0.5)

        if heads_count in results:
            results[heads_count] += 1
        else:
            results[heads_count] = 1

    percent = {key: (value / trials * 100) for key, value in results.items()}

    return percent


def draw_gaussian_distribution_graph() -> None:
    flip_statistics = flip_coin()
    xpoints = np.array(sorted(list(flip_statistics.keys())))
    ypoints = np.array(sorted(list(flip_statistics.values())))

    plt.plot(xpoints, ypoints)
    plt.title("Gaussian distribution graph")
    plt.xlabel("Heads number")
    plt.ylabel("Percentages")
    plt.show()
