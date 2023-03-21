import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for i in range(10000):
        heads_count = 0
        for _ in range(10):
            flip = random.choice([0, 1])
            if flip == 1:
                heads_count += 1
        results[heads_count] += 1
    for key, value in results.items():
        results[key] = (value / 10000) * 100
    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_points = [heads_count for heads_count in results.keys()]
    y_points = [drop_percentage for drop_percentage in results.values()]

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(x_points, y_points)

    plt.show()
