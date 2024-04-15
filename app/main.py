import random

import matplotlib.pyplot as plt

import numpy as np


def flip_coin() -> dict:
    result_dict = {
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
        10: 0,
    }
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            toss = random.choice(["head", "back"])
            if toss == "head":
                heads += 1
        if heads == 0:
            result_dict[0] += 1
        if heads == 1:
            result_dict[1] += 1
        if heads == 2:
            result_dict[2] += 1
        if heads == 3:
            result_dict[3] += 1
        if heads == 4:
            result_dict[4] += 1
        if heads == 5:
            result_dict[5] += 1
        if heads == 6:
            result_dict[6] += 1
        if heads == 7:
            result_dict[7] += 1
        if heads == 8:
            result_dict[8] += 1
        if heads == 9:
            result_dict[9] += 1
        if heads == 10:
            result_dict[10] += 1

    for key in result_dict:
        result_dict[key] /= 100
    print(result_dict)
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    dict_of_data = flip_coin()
    wxx = np.array(list(dict_of_data.keys()))
    wyy = np.array(list(dict_of_data.values()))
    plt.plot(wxx, wyy)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
