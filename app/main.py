import random

import numpy as np

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    total_trials = 10000
    for _ in range(total_trials):
        heads_count = sum(1 for _ in range(10) if random.random() < 0.5)
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / total_trials) * 100, 2)

    return results


print(flip_coin())


def draw_gaussian_distribution_graph(result: dict) -> None:
    xline = np.array([result.key()])
    yline = np.array([result.value()])

    plt.plot(xline, yline)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage%")
    plt.show()
