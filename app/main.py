import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    num_simulations = 10000
    results = {}

    for _ in range(num_simulations):
        num_heads = sum(random.randint(0, 1) for _ in range(10))
        results[num_heads] = results.get(num_heads, 0) + 1

    for key in results:
        results[key] = (results[key] / num_simulations) * 100

    return results


def draw_gaussian_distribution_graph() -> None:
    xpoints = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ypoints = np.array([0, 1, 5, 15, 20, 25, 20, 15, 5, 1, 0])

    plt.plot(xpoints, ypoints)
    plt.show()
