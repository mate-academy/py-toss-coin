import matplotlib.pyplot as plt

import random


def flip_coin() -> dict:
    res = {i: 0 for i in range(11)}

    for _ in range(10_000):
        ten_flips = [random.randint(0, 1) for i in range(10)]
        res[ten_flips.count(0)] += 1

    for key in res:
        res[key] = round(res[key] / 10_000 * 100, 2)

    return res


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x_values = list(data.keys())
    y_values = list(data.values())

    plt.ylim(0, 100)
    plt.plot(x_values, y_values)

    plt.title("10_000 coin flip normal distribution")

    plt.show()
