import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads_count = 0
        for i in range(10):
            heads_count += random.randint(0, 1)
        result[heads_count] += 1
    for key in result:
        result[key] /= 100
    return result


def draw_gaussian_distribution_graph() -> None:
    plt.plot(list(flip_coin().keys()), list(flip_coin().values()))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads counts")
    plt.ylabel("Drop persentage %")

    plt.show()
