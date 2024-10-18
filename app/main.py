import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    for _ in range(10000):
        count = 0
        for i in range(10):
            count += random.randint(0, 1)
        result_dict[count] += 1

    for i in range(11):
        result_dict[i] = round(
            result_dict[i] / 10000 * 100, 2
        )

    return result_dict


def draw_gaussian_distribution_graph() -> None:
    point_dict = flip_coin()
    x_array = []
    y_array = []
    for key, value in point_dict.items():
        x_array.append(key)
        y_array.append(value)

    xpoints = np.array(x_array)
    ypoints = np.array(y_array)

    plt.plot(xpoints, ypoints)
    plt.show()
