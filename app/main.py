import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1):
                heads += 1
        result[heads] += 1
    for key, value in result.items():
        result[key] = round(value / 100, 2)
    return result


def draw_gaussian_distribution_graph() -> None:
    for heads, count in flip_coin():
        xpoints = np.array([heads])
        ypoints = np.array([count])

        plt.plot(xpoints, ypoints)
        plt.show()
