import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    result_of_bars = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }

    count_of_bars = 10000
    result_of_percentage = {}
    coin = ["heads", "tails"]
    for _ in range(count_of_bars):
        quantity_of_heads = 0
        for _ in range(10):
            if random.choice(coin) == "heads":
                quantity_of_heads += 1
        result_of_bars[quantity_of_heads] += 1

    for element in result_of_bars:
        result_of_percentage[element] = round(
            result_of_bars.get(element) / count_of_bars * 100, 2
        )

    return result_of_percentage


def draw_gaussian_distribution_graph(result_of_percentage: dict):
    xpoints = np.array([key for key in result_of_percentage.keys()])
    ypoints = np.array([value for value in result_of_percentage.values()])

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop Percentage %")

    plt.show()
