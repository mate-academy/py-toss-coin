import random
import numpy
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000, flips: int = 10) -> dict:
    result = {i: 0 for i in range(flips + 1)}
    for i in range(cases):
        head_counts = sum(random.choice([0, 1]) for _ in range(flips))
        result[head_counts] += 1
    percentage = {
        key: round(value / cases * 100, 2)
        for key, value in result.items()
    }
    return percentage


def draw_gaussian_distribution_graph(flip_dict: dict) -> None:
    x_axis = list(flip_dict.keys())
    y_axis = list(flip_dict.values())

    xpoints = numpy.array(x_axis)
    ypoints = numpy.array(y_axis)

    plt.plot(xpoints, ypoints)
    plt.xticks(xpoints)
    plt.grid()
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
