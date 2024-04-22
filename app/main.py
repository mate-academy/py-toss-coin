from random import choices

import numpy as np

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    sides_of_coin = ["head", "tail"]
    for _ in range(10001):
        times = choices(sides_of_coin, k=10)
        for key in heads.keys():
            if key == times.count("head"):
                heads[key] += 1

    for key_, value in heads.items():
        heads[key_] = value / 100
    return heads


def draw_gaussian_distribution_graph() -> None:
    graphic_dict = flip_coin()

    line_x = np.array(list(graphic_dict.keys()))
    line_y = np.array(list(graphic_dict.values()))

    plt.plot(line_x, line_y)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
