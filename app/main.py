import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.choice(coin) == "heads":
                heads += 1
        result[heads] += 1
    for key, value in result.items():
        result[key] = value / 100
    return result


def draw_gaussian_distribution_graph() -> None:
    coords = flip_coin()
    x_arr = []
    y_arr = []
    for key, value in coords.items():
        x_arr.append(key)
        y_arr.append(value)
    x = np.array(x_arr)  # noqa 001
    y = np.array(y_arr)  # noqa 001
    plt.plot(x, y)
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
