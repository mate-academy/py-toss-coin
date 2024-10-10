import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {}

    for _ in range(10000):
        counter = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            if flip:
                counter += 1
        if counter not in result_dict:
            result_dict[counter] = 1
        else:
            result_dict[counter] += 1

    sorted_dict = dict(sorted(result_dict.items())).items()
    return {key: (value / 10000) * 100 for key, value in sorted_dict}


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
