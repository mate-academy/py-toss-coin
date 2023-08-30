import random
import matplotlib as plt
import numpy as np


def flip_coin() -> dict:
    res_dict = {num: 0 for num in range(11)}
    for _ in range(10000):
        action = random.gauss(5, 1.6)
        if action < 0:
            res_dict[0] += round(1 / 1000, 2)
            continue
        elif action > 10:
            res_dict[10] += round(1 / 1000, 2)
            continue
        res_dict[round(action)] += round(1 / 100, 2)
    return res_dict


def draw_gaussian_distribution_graph() -> None:
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Percentage")

    coin_flips = flip_coin()

    x_points = np.array(list(coin_flips.keys()))
    y_points = np.array(list(coin_flips.values()))

    plt.plot(x_points, y_points)

    plt.xticks(np.arange(0, 11))
    plt.yticks(np.arange(0, 101, 10))

    plt.show()
