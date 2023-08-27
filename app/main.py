from random import randint
import numpy as np
from matplotlib import pyplot as plt


def flip_coin(num_cases: int = 10000) -> dict:
    results = {}

    for _ in range(num_cases):
        num_heads = sum(randint(0, 1) for _ in range(10))
        results[num_heads] = results.get(num_heads, 0) + 1

    percentages = {
        key: (value / num_cases) * 100
        for key, value in results.items()
    }

    sorted_percentages = {
        key: percentages.get(key, 0)
        for key in range(11)
    }

    return sorted_percentages


def draw_gaussian_distribution_graph() -> None:
    flips = flip_coin()

    x_points = np.array(list(flips.keys()))
    y_points = np.array(list(flips.values()))

    plt.plot(x_points, y_points)

    plt.xticks(np.arange(0, 11))
    plt.yticks(np.arange(0, 101, 10))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Percentage")

    plt.show()
