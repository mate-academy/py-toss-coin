import random

import numpy as np

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    res_dict = {}
    count_flip = 0

    while count_flip < 10001:
        buf_count = 0
        for _ in range(10):
            if random.choice([0, 1]):
                buf_count += 1
        res_dict_value = res_dict.get(buf_count, 0)
        res_dict[buf_count] = res_dict_value + 1
        count_flip += 1

    for key in res_dict:
        res_dict[key] = round(res_dict[key] / 100, 2)
    return res_dict


def draw_gaussian_distribution_graph() -> None:
    date_dict = flip_coin()
    x_axis = np.array(list(date_dict.keys()))
    y_axis = np.array(list(date_dict.values()))

    plt.plot(x_axis, y_axis)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


draw_gaussian_distribution_graph()
