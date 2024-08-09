import random

import matplotlib.pyplot as plt
from matplotlib import ticker


def flip_coin() -> dict:
    count_runs = 100_000
    statistics = {x: 0.0 for x in range(11)}
    for current_run in range(count_runs):
        lucky_throw = 0
        for throw in range(10):
            if random.choice(["head", "tails"]) == "head":
                lucky_throw += 1
        statistics[lucky_throw] += 1
    for key_number, lucky_throw in statistics.items():
        statistics[key_number] = lucky_throw * 100 / count_runs
    return statistics


def draw_gaussian_distribution_graph(static: dict) -> None:
    axis_x = list(static.keys())
    axis_y = list(static.values())
    plt.plot(axis_x, axis_y)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    current_axis = plt.gca()
    current_axis.xaxis.set_major_locator(ticker.MultipleLocator(1))
    current_axis.yaxis.set_major_locator(ticker.MultipleLocator(10))

    current_axis.yaxis.set_minor_locator(ticker.MultipleLocator(5))

    plt.show()


draw_gaussian_distribution_graph(flip_coin())
