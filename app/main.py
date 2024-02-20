import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    result = {}
    for _ in range(10000):
        counter = 0
        for _ in range(10):
            if random.choice(coin) == "heads":
                counter += 1
        result[counter] = result.get(counter, 0) + 1
    return {
        key: value / 100 for key, value in result.items()
    }


def draw_gaussian_distribution_graph(coin_distribution: dict) -> None:
    distribution = dict(sorted(coin_distribution.items()))
    xpoints = np.array(list(distribution.keys()))
    ypoints = np.array(list(distribution.values()))

    plt.plot(xpoints, ypoints)
    plt.show()
