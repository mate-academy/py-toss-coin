import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    num_cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        coin_flips = [random.choice(["Heads", "Tails"]) for _ in range(10)]

        num_heads = coin_flips.count("Heads")

        results[num_heads] += 1

    percentages = {key: (value / num_cases) * 100 for key, value
                   in results.items()}

    return percentages


def draw_gaussian_distribution_graph() -> None:
    xpoints = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ypoints = np.array([0, 1, 5, 15, 20, 25, 20, 15, 5, 1, 0])

    plt.plot(xpoints, ypoints)
    plt.show()
