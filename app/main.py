import random
import matplotlib.pyplot as plt
import numpy as np
from typing import Callable


def flip_coin() -> dict:
    result = {}
    for _ in range(10_000):
        heads_count = 0
        for _ in range(10):
            choice = random.choice(("head", "tail"))
            if choice == "head":
                heads_count += 1

        if result.get(heads_count):
            result[heads_count] += 1
        else:
            result[heads_count] = 1

    result = {key: (value / 100) for key, value in result.items()}
    sorted_points = dict(sorted(result.items()))
    return sorted_points


def draw_gaussian_distribution_graph(func: Callable) -> None:
    points = func()

    x_points = np.array(list(points.keys()))
    y_points = np.array(list(points.values()))

    plt.plot(x_points, y_points)
    plt.show()
