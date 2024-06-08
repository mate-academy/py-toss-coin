import random

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def flip_coin() -> dict:
    number_of_cases = 10000

    numbers_of_flips = {
        i: 0
        for i in range(11)
    }

    for _ in range(number_of_cases):
        head_count = 0

        for _ in range(10):
            head = random.randint(0, 1)
            if head:
                head_count += 1

        numbers_of_flips[head_count] += 1

    percents_of_flipping = {
        i: round(numbers_of_flips[i] / number_of_cases * 100, 2)
        for i in range(11)
    }

    return percents_of_flipping


def draw_gaussian_distribution_graph(percents_of_flipping: dict) -> None:
    x_axis = np.array([
        key for key in percents_of_flipping.keys()
    ])

    y_axis = np.array([
        value for value in percents_of_flipping.values()
    ])

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.plot(x_axis, y_axis)

    y_ticks = np.arange(0, 101, 10)
    plt.yticks(y_ticks)
    plt.xticks(np.arange(0, 11, 1))

    plt.minorticks_on()
    plt.gca().yaxis.set_minor_locator(MultipleLocator(5))
    plt.gca().xaxis.set_minor_locator(MultipleLocator())

    plt.show()
