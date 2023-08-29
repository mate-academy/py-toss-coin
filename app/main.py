import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    cases = 10000
    flips = 10
    attempts = {flip: 0 for flip in range(flips + 1)}

    for case in range(cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(flips))
        attempts[heads_count] += 1

    for key, value in attempts.items():
        attempts[key] = value * 100 / cases

    return attempts


def draw_gaussian_distribution_graph() -> None:
    odds = flip_coin()
    print(odds)
    x_points = np.array(list(odds.keys()))
    y_points = np.array(list(odds.values()))

    plt.plot(x_points, y_points)
    plt.show()
