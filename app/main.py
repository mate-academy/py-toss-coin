import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for i in range(10_000):
        result[len([1 for _ in range(10) if random.choice([1, 0]) == 1])] += 1
    return {key: round(value / 100, 2) for key, value in result.items()}


def draw_gaussian_distribution_graph(coin_guess: dict) -> None:
    yaxis = np.array([value for value in coin_guess.values()])
    xaxis = np.array([key for key in coin_guess.keys()])
    plt.plot(xaxis, yaxis)

    ax = plt.gca()
    ax.set_ylim([0, 100])
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))

    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.title("Gaussian distribution")

    plt.show()
