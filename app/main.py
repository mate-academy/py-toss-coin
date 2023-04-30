import matplotlib.pyplot as plt

import numpy as np

import random


def flip_coin() -> dict:
    cases_of_flipping = 10000
    result = {}
    result_absolut = {number: 0 for number in range(0, 11)}
    for i in range(0, cases_of_flipping):
        number = 0
        for _ in range(0, 10):
            number += random.randint(0, 1)
        result_absolut[number] += 1

    for number_abs, value_abs in result_absolut.items():
        result[number_abs] = round(value_abs * (100 / cases_of_flipping), 2)

    return result


def draw_gaussian_distribution_graph(graf: dict) -> None:
    xpoints = []
    ypoints = []
    for keys, values in graf.items():
        xpoints.append(keys)
        ypoints.append(values)

    plt.plot(np.array(xpoints), np.array(ypoints))
    plt.show()
