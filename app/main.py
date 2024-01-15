import random
from decimal import Decimal
import matplotlib.pyplot as plt
from typing import Callable


def flip_coin(
        cases: int = 10000,
        flips: int = 10
) -> dict:
    results = {}
    for _ in range(cases):
        heads_up = sum(random.choice([0, 1]) for _ in range(flips))

        if heads_up not in results:
            results[heads_up] = 0

        results[heads_up] += 1

    percentage = {
        key: round(Decimal(str((value / cases) * 100)), 2)
        for key, value in results.items()
    }
    return percentage


def draw_gaussian_distribution_graph(flip_coin: Callable) -> None:
    data = flip_coin()
    data_sorted = dict(sorted(data.items()))

    x_points = list(data_sorted.keys())
    y_points = list(data_sorted.values())

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.plot(x_points, y_points)
    plt.show()


draw_gaussian_distribution_graph(flip_coin)
