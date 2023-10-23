import matplotlib.pyplot as plt
import numpy as np

import random


def flip_coin(num_cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    # Convert counts to percentages
    total_cases = num_cases
    for key, value in results.items():
        results[key] = (value / total_cases) * 100

    return results


def draw_gaussian_distribution_graph() -> None:
    values_for_graph = flip_coin()
    xpoints = np.array(list(values_for_graph.keys()))
    ypoints = np.array(list(values_for_graph.values()))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(xpoints, ypoints)

    # Установка максимального значения оси y в 100
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.show()
