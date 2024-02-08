from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin_flips = {}

    for _ in range(10000):
        heads_count = sum(randint(0, 1) for _ in range(10))
        coin_flips[heads_count] = coin_flips.get(heads_count, 0) + 1

    percents = {key: (value / 10000) * 100 for key,
                value in coin_flips.items()}

    return percents


def draw_gaussian_distribution_graph(data: dict) -> None:
    keys, values = zip(*sorted(data.items()))
    plt.bar(keys, values, align="center", color="red")
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.show()
