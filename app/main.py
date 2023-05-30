import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    num_cases = 10000
    num_flips = 10

    results = {}
    for i in range(num_cases):
        heads_count = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                heads_count += 1

        if heads_count in results:
            results[heads_count] += 1
        else:
            results[heads_count] = 1

    percentages = {}
    for heads, count in results.items():
        percentage = (count / num_cases) * 100
        percentages[heads] = percentage

    return percentages


def draw_gaussian_distribution_graph() -> None:
    for heads, count, limit in flip_coin():
        xpoints = np.array([heads])
        ypoints = np.array([count])

        plt.plot(xpoints, ypoints)
        plt.show()
