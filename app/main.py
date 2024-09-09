from random import choice
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    trials = 10000
    result = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads_count = sum(choice([0, 1]) for _ in range(10))
        result[heads_count] += 1

    for key in result:
        result[key] = (result[key] / trials) * 100

    return result


def draw_gaussian_distribution_graph() -> None:
    points_dict = flip_coin()

    x_axis = np.array(list(points_dict.keys()))
    y_axis = np.array(list(points_dict.values()))

    plt.plot(x_axis, y_axis)

    plt.title("Heads count")
    plt.xlabel("Drop percentage %")
    plt.ylabel("Gaussian distribution")

    plt.show()
