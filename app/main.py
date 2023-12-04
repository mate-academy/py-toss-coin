import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = dict.fromkeys(range(11), 0)
    number_of_cases = 45000
    for i in range(number_of_cases):
        heads = sum([random.choice((0, 1)) for j in range(10)])
        result[heads] += 1

    for occurences in result:
        result[occurences] /= (number_of_cases / 100)

    return result


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_points = list(data.keys())
    y_points = list(data.values())
    plt.plot(x_points, y_points)
    plt.show()
