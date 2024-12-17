import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000, times: int = 10) -> dict:
    count = {i: 0 for i in range(times + 1)}

    for _ in range(cases):
        ran = sum([random.choice([0, 1]) for _ in range(times)])
        count[ran] += 1

    count_percent = {
        key: round((value / cases) * 100, 2) for key, value in count.items()
    }
    return count_percent


def draw_gaussian_distribution_graph(count_percent: dict) -> None:

    x_axis = np.array([num for num in range(11)])
    y_axis = np.array([percent for percent in count_percent.values()])

    plt.plot(x_axis, y_axis)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
