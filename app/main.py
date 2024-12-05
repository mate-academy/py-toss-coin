import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {}
    tries = 10000
    flip_results = []

    for _ in range(tries):
        ten_flips = sum(random.choice([0, 1]) for _ in range(10))
        flip_results.append(ten_flips)

    for i in range(10 + 1):
        result[i] = flip_results.count(i) / tries * 100
    return result


def draw_gaussian_distribution_graph() -> None:
    x_points = np.array(range(10 + 1))
    y_points = np.array(list(flip_coin().values()))

    plt.plot(x_points, y_points)
    plt.title("Flip_coin_graph")
    plt.xlabel("Tail of coin")
    plt.ylabel("Percentage")
    plt.show()
