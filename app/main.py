import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0

    }
    for _ in range(10000):
        count = 0
        for _ in range(10):
            variant = random.choice(["heads", "tails"])
            if variant == "heads":
                count += 1
        result[count] += 1
    return {key: round((value / 100), 2) for key, value in result.items()}


def draw_gaussian_distribution_graph() -> None:
    x_points = [key for key in flip_coin().keys()]
    y_points = [value for value in flip_coin().values()]
    print(y_points)

    xpoints = np.array(x_points)
    ypoints = np.array(y_points)

    plt.plot(xpoints, ypoints)
    plt.show()
