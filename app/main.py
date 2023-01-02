import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    coin_sides = ["heads", "tails"]
    total_distribution = {}
    for i in range(11):
        total_distribution[i] = 0

    for i in range(10000):
        result_10_flips = 0
        for _ in range(10):
            if random.choice(coin_sides) == "heads":
                result_10_flips += + 1
        total_distribution[result_10_flips] += 1

    total_distribution_percent = {}
    for i in range(11):
        total_distribution_percent[i] = round(
            (total_distribution[i] / 10000 * 100), 3
        )

    return total_distribution_percent


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    keys = distribution.keys()
    values = distribution.values()

    plt.plot(keys, values)
    plt.ylim(0, 100)
    plt.show()
