import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    result_list = []

    for i in range(10000):
        result_flip = 0
        for _ in range(10):
            result_flip += random.randint(0, 1)
        result_list.append(result_flip)

    for toss_count in result_dict:
        result_dict[toss_count] = round(
            (result_list.count(toss_count) / 10000 * 100), 2
        )

    return result_dict


def draw_gaussian_distribution_graph(dictionary: dict) -> None:
    y_coord = np.array([value for value in dictionary.values()])
    x_coord = np.array([key for key in dictionary.keys()])

    font2 = {"family": "serif", "color": "darkred", "size": 17}

    plt.xlabel("Chance of head coin", fontdict=font2)
    plt.ylabel("Toss Count", fontdict=font2)
    plt.plot(x_coord, y_coord)
    plt.show()
