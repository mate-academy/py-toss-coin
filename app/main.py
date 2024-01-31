import random

import numpy as np

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    dict_of_variations = {i: i for i in range(11)}

    for i in range(10000):
        i = sum([random.randint(0, 1) for i in range(0, 10)])
        dict_of_variations[i] += 1

    for i in range(0, len(dict_of_variations)):
        dict_of_variations[i] /= 100

    return dict_of_variations


def draw_gaussian_distribution_graph() -> None:
    dict_of_variations = flip_coin()
    y_line = np.array([i for i in dict_of_variations.values()])
    x_line = np.array(list(i for i in range(11)))
    plt.plot(x_line, y_line)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


draw_gaussian_distribution_graph()
