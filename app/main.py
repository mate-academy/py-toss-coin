import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    resoults = {}
    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        resoults[heads_count] = resoults.get(heads_count, 0) + 1
    calculate_resoults = {key: round(((value / 10000) * 100), 2)
                          for key, value in resoults.items()}
    calculate_resoults = dict(sorted(calculate_resoults.items()))
    return calculate_resoults


def draw_gaussian_distribution_graph(flip_coin: dict = flip_coin()) -> None:
    x_cor = list(flip_coin.keys())
    y_cor = list(flip_coin.values())

    plt.plot(x_cor, y_cor)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")

    plt.show()
