from random import randint
import numpy as np

import matplotlib.pyplot as plt


def flip_coin() -> dict[float]:
    heads = {i: 0 for i in range(11)}
    for i in range(10000):
        flipping = [randint(0, 1) for _ in range(10)].count(0)
        heads[flipping] += 1
    heads = {head: percent / 100 for head, percent in heads.items()}
    return heads


def draw_gaussian_distribution_graph() -> None:
    graphic = flip_coin()

    xpoints = np.array(list(graphic.keys()))
    ypoints = np.array(list(graphic.values()))

    plt.plot(xpoints, ypoints)

    plt.xlabel("Heads count")
    plt.ylabel("Percentage")

    plt.show()
