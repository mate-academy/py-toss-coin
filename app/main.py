import random

import matplotlib.pyplot as plt

import numpy


def flip_coin() -> dict:
    percent_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                count += 1
        percent_dict[count] += 1

    for key, value in percent_dict.items():
        percent_dict[key] = round((value / 10000) * 100, 2)
    return percent_dict


def draw_gaussian_distribution_graph(dict_of_data: dict) -> None:
    x_coordinate = numpy.array(dict_of_data.keys())
    y_coordinate = numpy.array(dict_of_data.values())

    plt.plot(x_coordinate, y_coordinate)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
