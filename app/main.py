import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = []
    flipping = {}
    counter = 10000
    while counter:
        flipping_random = random.randint(0, 10)
        result.append(flipping_random)
        counter -= 1

    for item in result:
        flipping[item] = result.count(item) / 100

    return dict(sorted(flipping.items()))


def draw_gaussian_distribution_graph() -> None:
    x_point = flip_coin().keys()
    y_point = flip_coin().values()

    plt.plot(x_point, y_point)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
