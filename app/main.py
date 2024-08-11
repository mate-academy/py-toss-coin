# import numpy as np
import matplotlib.pyplot as plt

import random


def flip_coin() -> dict:
    num_dict = {}

    for _ in range(10000):
        count_come_up = 0
        for __ in range(10):

            random_num = random.randint(0, 1)
            if random_num == 1:
                count_come_up += 1

        if count_come_up in num_dict:
            num_dict[count_come_up] += 1
        else:
            num_dict[count_come_up] = 1

    res_dict = {
        key: round((value / 10000) * 100, 2)
        for key, value in num_dict.items()
    }

    return res_dict


def draw_graph(statistic_dict: dict) -> None:
    sorted_dict = dict(sorted(statistic_dict.items()))
    # x_arr = np.array([int(key) for key in sorted_dict.keys()])
    # y_arr = np.array([value for value in sorted_dict.values()])
    x_arr = [int(key) for key in sorted_dict.keys()]
    y_arr = [value for value in sorted_dict.values()]

    plt.title("Gaussian distribution")
    plt.xlabel("Drop percentage %")
    plt.ylabel("Heads count")
    plt.ylim(0, 100)

    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))

    plt.plot(x_arr, y_arr)
    plt.show()
