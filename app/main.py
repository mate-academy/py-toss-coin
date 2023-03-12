import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    statistic = {i: 0 for i in range(11)}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            coin = ("averse", "reverse")
            count += 1 if random.choice(coin) == "averse" else False
        statistic[count] += 0.01
    return statistic


def draw_gaussian_distribution_graph() -> None:
    stat = flip_coin()
    x_array = np.array([heads for heads in stat])
    y_array = np.array([drop for drop in stat.values()])

    plt.plot(x_array, y_array)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
