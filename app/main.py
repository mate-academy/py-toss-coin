import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    results = {}
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1
        if heads_count in results:
            results[heads_count] += 1
        else:
            results[heads_count] = 1
    percentages = {key: value / 100 for key, value in results.items()}
    return percentages


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    x_coord = list(results.keys())
    y_coord = list(results.values())

    plt.plot(x_coord, y_coord, marker="o", linestyle="-")
    plt.xlabel()
    plt.ylabel()
    plt.title()
    x_smooth = np.linspace(min(x_coord), max(x_coord), 100)
    y_smooth = np.interp(x_smooth, x_coord, y_coord)
    plt.plot(x_smooth, y_smooth)

    plt.grid(True)
    plt.show()
