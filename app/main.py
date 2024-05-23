import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(num: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}
    if num < 10000:
        num = 10000
    for i in range(num):
        heads = 0
        for _ in range(10):
            heads += random.choice([0, 1])
        results[heads] += 1

    results = {key: (value / num) * 100 for key, value in results.items()}

    return results


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    x_points = np.array(list(results.keys()))
    y_points = np.array(list(results.values()))

    plt.plot(x_points, y_points)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
