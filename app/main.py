from random import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    work_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for i_thousand in range(9999):
        side_coin_decade = 0
        for j_decades in range(10):
            side_coin = 0
            if random() >= 0.5:
                side_coin = 1
            side_coin_decade += side_coin
        work_dict[side_coin_decade] += 1
    result_dict = {}
    for work in work_dict:
        result_dict[work] = round(work_dict[work] / 100, 2)

    return result_dict


def draw_gaussian_distribution_graph(data_for_graph: dict[float]) -> None:
    list_x = []
    list_y = []
    for work in data_for_graph:
        list_x.append(work)
        list_y.append(data_for_graph[work])
    x_axis = np.array(list_x)
    y_axis = np.array(list_y)

    plt.plot(x_axis, y_axis)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
