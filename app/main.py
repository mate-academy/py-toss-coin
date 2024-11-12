import random
import numpy as np
import matplotlib.pyplot as plt

from collections import Counter


def flip_coin() -> dict:
    count_heads = Counter(
        sum(random.randint(0, 1) for _ in range(10)) for _ in range(10000)
    )
    heads_percentage = {
        head: round(percent / 10000 * 100, 2)
        for head, percent in count_heads.items()
    }
    return heads_percentage


def draw_gaussian_distribution_graph() -> None:
    gaussian_distribution = sorted(flip_coin().items())
    heads = [i[0] for i in gaussian_distribution]
    percentages = [i[1] for i in gaussian_distribution]

    plt.plot(heads, percentages, color="blue")
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.yticks(range(0, 110, 10))
    plt.xticks(range(0, 11, 1))
    minor_ticks = np.arange(5, 105, 10)
    plt.minorticks_on()
    plt.yticks(minor_ticks, minor=True)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
