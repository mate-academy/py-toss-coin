from random import choice
import matplotlib.pyplot as plt
import numpy as np


DISTRIBUTION_WIDTH = 10000
CASE_WIDTH = 10
PERCENTAGE_FACTOR = DISTRIBUTION_WIDTH // 100


def flip_coin() -> dict:
    distribution = {i: 0 for i in range(CASE_WIDTH + 1)}
    for _ in range(DISTRIBUTION_WIDTH):
        heads = 0
        for _ in range(CASE_WIDTH):
            heads += choice((0, 1))
        distribution[heads] += 1

    return {i: value / PERCENTAGE_FACTOR for i, value in distribution.items()}


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    x_axis = np.array(list(distribution.keys()))
    y_axis = np.array(list(distribution.values()))

    plt.ylim(0, 100)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Percentage, %")

    plt.plot(x_axis, y_axis)
    plt.grid()
    plt.show()
