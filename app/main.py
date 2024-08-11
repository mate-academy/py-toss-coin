import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    results = {i: 0 for i in range(10 + 1)}
    for i in range(10_000):
        heads_counter = 0
        for _ in range(10):
            coin_side = random.choice(["Heads", "Tails"])
            if coin_side == "Heads":
                heads_counter += 1
        results[heads_counter] += 1
    return {key: (value * 100) / 10_000 for key, value in results.items()}


def draw_gaussian_distribution_graph() -> None:
    coin_flip_results = flip_coin()
    x_points = np.array(coin_flip_results.keys())
    y_points = np.array(coin_flip_results.values())

    plt.plot(x_points, y_points)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
