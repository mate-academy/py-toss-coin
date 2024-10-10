import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        counter = sum(random.choice([0, 1]) for i in range(10))
        result_dict[counter] += 1

    return {key: (value / 10000) * 100 for key, value in result_dict.items()}


def draw_gaussian_distribution_graph(points: dict) -> None:
    x_axis = list(points.keys())
    y_axis = list(points.values())
    plt.plot(x_axis, y_axis)

    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
