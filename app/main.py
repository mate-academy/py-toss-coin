import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict[int, float]:
    heads_list = [sum(random.choices([1, 0], k=10)) for _ in range(10000)]

    heads_occurrence = {}
    for number in range(11):
        heads_occurrence[number] = heads_list.count(number) / 100

    return heads_occurrence


def draw_gaussian_distribution_graph() -> None:
    heads_stats = flip_coin()
    x_coord = np.array(heads_stats.keys())
    y_coord = np.array(heads_stats.values())

    plt.plot(x_coord, y_coord, color="orange")
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
