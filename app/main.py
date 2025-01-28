import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    final_dict = {
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
    for attempts in range(10001):
        count = 0
        for attempt in range(10):
            head = (random.randint(1, 2))
            if head == 1:
                count += 1
        final_dict[count] += (1 / 10001) * 100
    return {num: round(value, 2) for num, value in final_dict.items()}


def draw_gaussian_distribution_graph(plots: dict) -> None:
    xplots = np.array(plots.keys())
    yplots = np.array(plots.values())

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(xplots, yplots)
    plt.show()
