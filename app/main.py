import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_out = sum(random.randint(0, 1) for _ in range(10))
        result[heads_out] += 1

    percents = {key: round(value / 10000.0 * 100, 2)
                for key, value in result.items()}
    # draw_gaussian_distribution_graph(percents)
    return percents


def draw_gaussian_distribution_graph(percents: dict) -> None:
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    perc_key = [key for key in percents]
    perc_value = [value for value in percents.values()]

    x_value = np.array(perc_key)
    y_value = np.array(perc_value)

    plt.ylim(0, 100)

    plt.plot(x_value, y_value, color="blue")
    plt.show()
